import re


class Settings:
    # is_dry_run and post_check_frequency_mins should not be overridden
    # set to True to prevent any bot actions (report, remove, comments)
    is_dry_run = False
    post_check_frequency_mins = 1

    report_location_statement_timeout = True

    post_check_threshold_mins = 2 * 60
    consecutive_old_posts = 5

    location_statement_time_limit_mins = 30

    sightings_flair = ["sightings report"]
    ls_removal_reason = ("Your post has been removed for not including a location statement, "
                         "meaning post text or a comment on your own post that provides location for the link. "
                         "If you still wish to share your post you must resubmit your link "
                         "accompanied by a location statement."
                         "\n\n"
                         "This is a bot. Replies will not receive responses. "
                         "Please message the moderators if you feel this was an error.")

    google_sheet_id = "1Ewy0BZxaafdWulW7Vd8NQCA6u7OJ0-gCYIPeTDNgmZA"
    google_sheet_name = "Sightings"


class SettingsFactory:
    settings_classes = {
        'ufos': Settings,
        'collapsetesting': Settings,
    }

    @staticmethod
    def get_settings(subreddit_name):
        # ensure only contains valid characters
        if not re.match(r'^\w+$', subreddit_name):
            raise ValueError("subreddit_name contains invalid characters")

        settings_class = SettingsFactory.settings_classes.get(subreddit_name.lower(), Settings)
        return settings_class()
