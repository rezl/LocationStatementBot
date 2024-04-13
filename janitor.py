import calendar
import re
import traceback
from datetime import datetime, timedelta
from enum import Enum

from post import Post


class Janitor:
    def __init__(self, discord_client, bot_username, reddit, reddit_handler, google_sheets_recorder, settings_map):
        self.discord_client = discord_client
        self.bot_username = bot_username
        self.reddit = reddit
        self.reddit_handler = reddit_handler
        self.google_sheets_recorder = google_sheets_recorder
        self.settings_map = settings_map

    @staticmethod
    def get_adjusted_utc_timestamp(time_difference_mins):
        adjusted_utc_dt = datetime.utcnow() - timedelta(minutes=time_difference_mins)
        return calendar.timegm(adjusted_utc_dt.utctimetuple())

    def fetch_new_posts(self, subreddit, settings):
        check_posts_after_utc = self.get_adjusted_utc_timestamp(settings.post_check_threshold_mins)

        submissions = list()
        consecutive_old = 0
        # posts are provided in order of: newly submitted/approved (from automod block)
        for post in subreddit.new():
            if post.created_utc > check_posts_after_utc:
                submissions.append(Post(post))
                consecutive_old = 0
            # old, approved posts can show up in new amongst truly new posts due to reddit "new" ordering
            # continue checking new until consecutive_old_posts are checked, to account for these posts
            else:
                submissions.append(Post(post))
                consecutive_old += 1

            if consecutive_old > settings.consecutive_old_posts:
                return submissions
        return submissions

    @staticmethod
    def validate_location_statement(location_statement):
        if not location_statement:
            return LocationStatementState.MISSING
        try:
            location = re.search(r'location: *(.*)\n', location_statement, re.IGNORECASE).group(1)
            time_seen = re.search(r'time: *(.*)\n', location_statement, re.IGNORECASE).group(1)
        except Exception as e:
            print(f"Exception {e} during keyword parsing. Marking invalid.")
            return LocationStatementState.INVALID
        if not location or not time_seen:
            return LocationStatementState.INVALID
        else:
            return LocationStatementState.VALID

    def handle_location(self, post, subreddit, settings):
        if not post.has_sightings_flair(settings):
            return
        if hasattr(post.submission, "saved") and post.submission.saved:
            # content saving is the way we persist whether the bot has seen/actioned this content
            return

        # order of preference: post text (self post or link post), then top-level OP comment
        location_statement = ''
        location_statement_state = LocationStatementState.MISSING
        # use link post's text if valid
        if post.submission.selftext != '':
            self_text = post.submission.selftext
            location_statement_state = Janitor.validate_location_statement(self_text)
            if location_statement_state == LocationStatementState.VALID:
                location_statement = self_text

        if not location_statement:
            location_statement = post.find_location_statement()
        if hasattr(location_statement, "body"):
            location_statement_state = Janitor.validate_location_statement(location_statement.body)
            location_statement = location_statement.body

        timeout_mins = settings.location_statement_time_limit_mins

        # users are given time to post a location statement
        if not post.is_post_old(timeout_mins):
            print("\tTime has not expired")
            return
        print("\tTime has expired")

        if location_statement_state == LocationStatementState.MISSING or \
                location_statement_state == LocationStatementState.INVALID:
            print(f"\tPost has {location_statement_state} location statement")
            if post.is_moderator_approved():
                self.reddit_handler.report_content(post.submission,
                                                   f"Moderator approved post, but is a {location_statement_state}"
                                                   f" location statement. Please look.")
            elif settings.report_location_statement_timeout:
                self.reddit_handler.report_content(post.submission,
                                                   f"Post has a {location_statement_state} location statement "
                                                   f"after timeout. Please look.")
            else:
                self.reddit_handler.remove_content(post.submission, settings.ls_removal_reason,
                                                   f"{location_statement_state} location statement")
        elif location_statement_state == LocationStatementState.VALID:
            self.reddit_handler.save_content(post.submission)
            print("\tPost has valid location statement")
            # sql injection?
            location = re.search(r'location: *(.*)\n', location_statement, re.IGNORECASE).group(1)
            time_seen = re.search(r'time: *(.*)\n', location_statement, re.IGNORECASE).group(1)
            sheet_values = [[location, time_seen]]
            self.google_sheets_recorder.append_to_sheet(subreddit.display_name, sheet_values)
        else:
            raise RuntimeError(f"\tUnsupported location_statement_state: {location_statement_state}")

    def handle_posts(self, subreddit):
        settings = self.settings_map[subreddit.display_name]
        posts = self.fetch_new_posts(subreddit, settings)
        print("Checking " + str(len(posts)) + " posts")
        for post in posts:
            print(f"Checking post: {post.submission.title}\n\t{post.submission.permalink}")

            try:
                self.handle_location(post, subreddit, settings)
            except Exception as e:
                message = f"Exception when handling post {post.submission.title}: {e}\n```{traceback.format_exc()}```"
                self.discord_client.send_error_msg(message)
                print(message)


class LocationStatementState(str, Enum):
    MISSING = "MISSING"
    INVALID = "INVALID"
    VALID = "VALID"
