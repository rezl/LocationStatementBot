import calendar
import gc
import re
import traceback
from datetime import datetime, timedelta
from enum import Enum

from post import Post


def has_date_component(text):
    """Check if text contains a SPECIFIC date - relative dates like 'yesterday' don't count"""
    if not text:
        return False
    patterns = [
        r'\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4}',  # 12/7/24, 12-7-2024, 12.7.24
        r'\d{1,2}[/\-\.]\d{1,2}',                 # 12/7, 12-7 (month/day without year)
        r'(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s*\d{1,2}',  # Dec 7, January 15
        r'\d{1,2}(?:st|nd|rd|th)?\s*(?:of\s+)?(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)',  # 7th Dec, 7 of January
    ]
    text_lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, text_lower):
            return True
    return False


def has_time_component(text):
    """Check if text contains a time-of-day pattern"""
    if not text:
        return False
    patterns = [
        r'\d{1,2}:\d{2}',                         # 8:30, 20:00
        r'\d{1,2}\s*(?:am|pm|a\.m\.|p\.m\.)',     # 8pm, 8 PM, 8 a.m.
        r'(?:morning|afternoon|evening|night|midnight|noon|dusk|dawn)',  # descriptive times
        r'around\s+\d{1,2}(?!\s*(?:th|st|nd|rd))',  # around 8 (but not "around 8th" which is a date)
    ]
    text_lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, text_lower):
            return True
    return False


def is_excluded_domain(domain, excluded_domains):
    """Check if domain is in the exclusion list (news sites, etc.)"""
    if not domain:
        return False
    domain_lower = domain.lower()
    for excluded in excluded_domains:
        if excluded in domain_lower:
            return True
    return False


def is_media_domain(domain, media_domains):
    """Check if domain indicates a media post (video/image)"""
    if not domain:
        return False
    domain_lower = domain.lower()
    for media in media_domains:
        if media in domain_lower:
            return True
    return False


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

    def handle_new_posts(self, subreddit, settings):
        check_posts_after_utc = self.get_adjusted_utc_timestamp(settings.post_check_threshold_mins)

        consecutive_old = 0
        # posts are provided in order of: newly submitted/approved (from automod block)
        for post in subreddit.new():
            # force gc to clean up previous post, if it existed, because ain't nobody got money for fly.io memory
            gc.collect()
            if post.created_utc > check_posts_after_utc:
                self.handle_post(post, subreddit, settings)
                consecutive_old = 0
            # old, approved posts can show up in new amongst truly new posts due to reddit "new" ordering
            # continue checking new until consecutive_old_posts are checked, to account for these posts
            else:
                self.handle_post(post, subreddit, settings)
                consecutive_old += 1

            if consecutive_old > settings.consecutive_old_posts:
                return
        return

    def handle_post(self, post, subreddit, settings):
        wrapped_post = Post(post)
        print(f"Checking post: {wrapped_post.submission.title}\n\t{wrapped_post.submission.permalink}")

        try:
            # First, try auto-flairing if enabled and post doesn't have sighting flair
            if settings.auto_flair_enabled and not wrapped_post.has_sightings_flair(settings):
                auto_flaired = self.handle_auto_flair(wrapped_post, subreddit, settings)
                if auto_flaired and not settings.auto_flair_dry_run:
                    # Post was just flaired - let it go through normal validation on next cycle
                    # (gives user time to add location statement if needed)
                    return
            
            # Then handle location validation for posts with sighting flair
            self.handle_location(wrapped_post, subreddit, settings)
        except Exception as e:
            message = f"Exception when handling post " \
                      f"{wrapped_post.submission.title},{wrapped_post.submission.permalink}: " \
                      f"{e}\n```{traceback.format_exc()}```"
            self.discord_client.send_error_msg(message)
            print(message)

    @staticmethod
    def validate_location_statement(location_statement):
        """
        Validates that a location statement contains properly formatted Time and Location fields.
        
        Returns:
            LocationStatementState.VALID - Both Time/Date and Location found with complete content
            LocationStatementState.MISSING - Required fields not found at all
            LocationStatementState.INVALID - Fields found but empty or malformed
            LocationStatementState.INCOMPLETE - Fields found but Time is missing date or time-of-day
        """
        if not location_statement:
            return LocationStatementState.MISSING
        
        # Try to extract time and location using improved patterns
        time_result = Janitor.get_time_capture(location_statement)
        location_result = Janitor.get_location_capture(location_statement)
        
        # Also check for split fields (e.g., separate Date: and Time: lines)
        all_datetime_content = Janitor.get_all_datetime_content(location_statement)
        
        # Debug logging to help diagnose issues
        print(f"\t[Validation] Time field: '{time_result}' | Location field: '{location_result}'")
        if all_datetime_content != time_result:
            print(f"\t[Validation] Combined date/time content: '{all_datetime_content}'")
        
        # Check if either field is completely missing (no match at all)
        if time_result is None and location_result is None:
            print(f"\t[Validation] MISSING - Neither Time nor Location field found")
            return LocationStatementState.MISSING
        
        if time_result is None:
            print(f"\t[Validation] MISSING - No Time/Date field found")
            return LocationStatementState.MISSING
            
        if location_result is None:
            print(f"\t[Validation] MISSING - No Location field found")
            return LocationStatementState.MISSING
        
        # Both fields exist, check if they have actual content
        time_content = time_result.strip()
        location_content = location_result.strip()
        
        # Require minimum content length (avoid "Time: ?" or "Location: .")
        min_content_length = 2
        
        if len(time_content) < min_content_length:
            print(f"\t[Validation] INVALID - Time field too short or empty: '{time_content}'")
            return LocationStatementState.INVALID
            
        if len(location_content) < min_content_length:
            print(f"\t[Validation] INVALID - Location field too short or empty: '{location_content}'")
            return LocationStatementState.INVALID
        
        # Check that date/time content contains BOTH a date and time-of-day component
        # Use combined content from all date/time fields (handles split Date: and Time: fields)
        content_to_check = all_datetime_content if all_datetime_content else time_content
        has_date = has_date_component(content_to_check)
        has_time = has_time_component(content_to_check)
        
        if not has_date or not has_time:
            missing = []
            if not has_date:
                missing.append("date")
            if not has_time:
                missing.append("time-of-day")
            print(f"\t[Validation] INCOMPLETE - Missing: {', '.join(missing)}")
            return LocationStatementState.INCOMPLETE
        
        print(f"\t[Validation] VALID - Time: '{time_content}' | Location: '{location_content}'")
        return LocationStatementState.VALID

    @staticmethod
    def get_all_datetime_content(location_statement):
        """
        Extract content from ALL Time/Date/When fields and combine them.
        This handles cases where users split info across separate Date: and Time: fields.
        
        Example: "Date: Dec 7th\nTime: 8pm" -> "Dec 7th 8pm"
        """
        if not location_statement:
            return None
        
        # Pattern to find all date/time field values
        pattern = r'\*{0,2}(?:time|date(?:/time)?|time/date|when)\*{0,2}[ \t]*[:\-\—\–][ \t]*\*{0,2}[ \t]*(.+?)(?=[ \t]*\*{0,2}(?:location|locaiton|loaction|locaton|where)|$|\n)'
        
        matches = re.findall(pattern, location_statement, re.IGNORECASE)
        
        if not matches:
            return None
        
        # Combine all captured values, clean up each one
        combined_parts = []
        for match in matches:
            cleaned = match.strip()
            cleaned = re.sub(r'^\*+\s*', '', cleaned)
            cleaned = re.sub(r'\s*\*+$', '', cleaned)
            if cleaned:
                combined_parts.append(cleaned)
        
        return ' '.join(combined_parts) if combined_parts else None

    @staticmethod
    def build_removal_reason(location_statement, state, settings):
        """
        Build a state-specific removal reason message.
        
        Args:
            location_statement: The text that was checked (for re-analyzing what's missing)
            state: The LocationStatementState
            settings: Settings object with message templates
            
        Returns:
            String with the appropriate removal reason for the user
        """
        # Determine the specific issue based on state
        if state == LocationStatementState.MISSING:
            specific_issue = settings.ls_issue_missing
        elif state == LocationStatementState.INVALID:
            specific_issue = settings.ls_issue_invalid
        elif state == LocationStatementState.INCOMPLETE:
            # For INCOMPLETE, figure out what specifically is missing
            time_result = Janitor.get_time_capture(location_statement) if location_statement else None
            if time_result:
                has_date = has_date_component(time_result)
                has_time = has_time_component(time_result)
                
                if not has_date and not has_time:
                    specific_issue = settings.ls_issue_incomplete_neither
                elif not has_date:
                    specific_issue = settings.ls_issue_incomplete_no_date
                elif not has_time:
                    specific_issue = settings.ls_issue_incomplete_no_time
                else:
                    # Shouldn't happen, but fallback
                    specific_issue = settings.ls_issue_incomplete_neither
            else:
                specific_issue = settings.ls_issue_incomplete_neither
        else:
            # Fallback - shouldn't happen for removal cases
            specific_issue = ""
        
        return settings.ls_removal_reason_template.format(specific_issue=specific_issue)

    @staticmethod
    def get_location_capture(location_statement):
        """
        Extract location value from statement. Handles various formats:
        - Location: somewhere (standard)
        - Where: somewhere (natural alternative)
        - Location- somewhere (hyphen instead of colon)
        - Location— somewhere (em dash from mobile keyboards)
        - Location– somewhere (en dash)
        - Locaiton: somewhere (common typo)
        - **Location:** somewhere (markdown bold)
        - *Location:* somewhere (markdown italic)
        
        Returns: The captured location string, or None if no match
        """
        # Pattern breakdown:
        # \*{0,2} - Optional markdown bold/italic (0-2 asterisks)
        # (?:location|...|where) - keyword variants and typos
        # \*{0,2} - Optional closing markdown
        # [ \t]* - Horizontal whitespace only (no newlines)
        # [:\-\—\–] - Colon, hyphen, em dash, or en dash as separator
        # [ \t]*\*{0,2}[ \t]* - Whitespace and optional markdown after separator
        # ([^\n]+) - Capture one or more non-newline characters
        pattern = r'\*{0,2}(?:location|locaiton|loaction|locaton|where)\*{0,2}[ \t]*[:\-\—\–][ \t]*\*{0,2}[ \t]*([^\n]+)'
        
        match = re.search(pattern, location_statement, re.IGNORECASE)
        if match:
            result = match.group(1).strip()
            # Remove leading/trailing markdown asterisks from captured content
            result = re.sub(r'^\*+\s*', '', result)  # Leading asterisks
            result = re.sub(r'\s*\*+$', '', result)  # Trailing asterisks
            return result.strip() if result.strip() else None
        return None

    @staticmethod
    def get_time_capture(location_statement):
        """
        Extract time/date value from statement. Handles various formats:
        - Time: 8pm (standard)
        - When: 8pm (natural alternative)
        - Time- 8pm (hyphen instead of colon)
        - Time— 8pm (em dash from mobile keyboards)
        - Time– 8pm (en dash)
        - Date: December 5, 2024
        - Date/Time: 12/5/24 8pm
        - Time/Date: 8pm 12/5/24
        - **Time:** 8pm (markdown bold)
        - *Date:* December 5 (markdown italic)
        
        Returns: The captured time/date string, or None if no match
        """
        # Pattern handles: time, date, when, date/time, time/date (with optional markdown)
        # Uses lookahead to stop capture at Location/Where keyword (for single-line entries)
        # [ \t]*\*{0,2}[ \t]* handles markdown asterisks after the separator
        pattern = r'\*{0,2}(?:time|date(?:/time)?|time/date|when)\*{0,2}[ \t]*[:\-\—\–][ \t]*\*{0,2}[ \t]*(.+?)(?=[ \t]*\*{0,2}(?:location|locaiton|loaction|locaton|where)|$|\n)'
        
        match = re.search(pattern, location_statement, re.IGNORECASE)
        if match:
            result = match.group(1).strip()
            # Remove leading/trailing markdown asterisks from captured content
            result = re.sub(r'^\*+\s*', '', result)  # Leading asterisks
            result = re.sub(r'\s*\*+$', '', result)  # Trailing asterisks
            return result.strip() if result.strip() else None
        return None

    # ==========================================================================
    # Auto-flair methods
    # ==========================================================================
    
    @staticmethod
    def should_auto_flair(post, settings):
        """
        Check if a post should be auto-flaired as a Sighting.
        
        Criteria:
        - Post does NOT already have Sighting flair
        - Post IS a media post (video/image)
        - Post is NOT from an excluded domain (news sites)
        - Post has Time/Location fields (even if incomplete - user gets 30 min to fix)
        
        Returns: (should_flair: bool, reason: str)
        """
        # Check if already has sighting flair
        if post.has_sightings_flair(settings):
            return False, "Already has Sighting flair"
        
        # Check if it's a media post (video/image)
        domain = getattr(post.submission, 'domain', '') or ''
        is_video = getattr(post.submission, 'is_video', False)
        
        if not is_video and not is_media_domain(domain, settings.auto_flair_media_domains):
            return False, f"Not a media post (domain: {domain})"
        
        # Check if domain is excluded (news sites)
        if is_excluded_domain(domain, settings.auto_flair_excluded_domains):
            return False, f"Excluded domain: {domain}"
        
        # Check for Time/Location fields (even incomplete is OK - user gets 30 min to fix)
        text_to_check = ""
        
        # Body (selftext)
        if post.submission.selftext:
            text_to_check = post.submission.selftext
        
        # Also include title
        text_to_check = text_to_check + "\n" + post.submission.title
        
        # Validate using the same logic as location statement validation
        location_statement_state = Janitor.validate_location_statement(text_to_check)
        
        if location_statement_state == LocationStatementState.VALID:
            time_captured = Janitor.get_time_capture(text_to_check)
            location_captured = Janitor.get_location_capture(text_to_check)
            return True, f"Valid data - Time: {time_captured}, Location: {location_captured}"
        elif location_statement_state == LocationStatementState.INCOMPLETE:
            # Has fields but missing date or time - auto-flair, user gets 30 min to fix
            time_captured = Janitor.get_time_capture(text_to_check)
            location_captured = Janitor.get_location_capture(text_to_check)
            return True, f"Incomplete data (user has 30 min to fix) - Time: {time_captured}, Location: {location_captured}"
        elif location_statement_state == LocationStatementState.INVALID:
            # Has fields but empty - auto-flair, user gets 30 min to fix
            return True, "Fields found but empty (user has 30 min to fix)"
        elif location_statement_state == LocationStatementState.MISSING:
            # No attempt at Time/Location fields - don't auto-flair
            return False, "No Time:/Location: fields found"
        else:
            return False, f"Unknown state: {location_statement_state}"
    
    def handle_auto_flair(self, post, subreddit, settings):
        """
        Check if post should be auto-flaired and apply flair if appropriate.
        
        Returns: True if post was flaired (or would be in dry run), False otherwise
        """
        if not settings.auto_flair_enabled:
            return False
        
        # Skip posts that are already saved (already processed)
        if hasattr(post.submission, "saved") and post.submission.saved:
            return False
        
        should_flair, reason = self.should_auto_flair(post, settings)
        
        if not should_flair:
            print(f"\t[Auto-flair] Skip: {reason}")
            return False
        
        # Apply flair
        if settings.auto_flair_dry_run:
            print(f"\t[Auto-flair] DRY RUN - Would flair as '{settings.auto_flair_text}': {reason}")
            self.discord_client.send_action_msg(
                f"[DRY RUN] Would auto-flair as **{settings.auto_flair_text}**:\n"
                f"**Title:** {post.submission.title}\n"
                f"**Reason:** {reason}\n"
                f"**Link:** https://reddit.com{post.submission.permalink}"
            )
            return True
        else:
            try:
                # Apply the flair
                post.submission.flair.select(flair_text=settings.auto_flair_text)
                print(f"\t[Auto-flair] Applied '{settings.auto_flair_text}' flair: {reason}")
                self.discord_client.send_action_msg(
                    f"Auto-flaired as **{settings.auto_flair_text}**:\n"
                    f"**Title:** {post.submission.title}\n"
                    f"**Reason:** {reason}\n"
                    f"**Link:** https://reddit.com{post.submission.permalink}"
                )
                return True
            except Exception as e:
                print(f"\t[Auto-flair] Error applying flair: {e}")
                self.discord_client.send_error_msg(
                    f"Failed to auto-flair post:\n"
                    f"**Title:** {post.submission.title}\n"
                    f"**Error:** {e}"
                )
                return False

    # ==========================================================================
    # Location validation methods
    # ==========================================================================

    def handle_location(self, post, subreddit, settings):
        if not post.has_sightings_flair(settings):
            print("Post does not have required flair")
            return
        if hasattr(post.submission, "saved") and post.submission.saved:
            # content saving is the way we persist whether the bot has seen/actioned this content
            print("Post has already been actioned - to re-action, unsave this post in the bot's account")
            return

        # order of preference: post body, then OP comment, then title
        location_statement = ''
        location_statement_state = LocationStatementState.MISSING
        location_statement_source = 'none'
        
        # 1. Check post body (selftext) first
        if post.submission.selftext != '':
            self_text = post.submission.selftext
            print(f"\t[Source] Checking post selftext ({len(self_text)} chars)")
            location_statement_state = Janitor.validate_location_statement(self_text)
            if location_statement_state == LocationStatementState.VALID:
                location_statement = self_text
                location_statement_source = 'selftext'

        # 2. If selftext didn't have valid statement, check OP comments
        if not location_statement:
            print(f"\t[Source] Checking OP comments for location statement")
            comment_statement = post.find_location_statement()
            if comment_statement and hasattr(comment_statement, "body"):
                print(f"\t[Source] Found OP comment ({len(comment_statement.body)} chars)")
                location_statement_state = Janitor.validate_location_statement(comment_statement.body)
                if location_statement_state == LocationStatementState.VALID:
                    location_statement = comment_statement.body
                    location_statement_source = 'comment'
            else:
                print(f"\t[Source] No OP comment with 'location' keyword found")

        # 3. If still no valid statement, check title
        if not location_statement:
            title = post.submission.title
            print(f"\t[Source] Checking post title: '{title}'")
            location_statement_state = Janitor.validate_location_statement(title)
            if location_statement_state == LocationStatementState.VALID:
                location_statement = title
                location_statement_source = 'title'

        timeout_mins = settings.location_statement_time_limit_mins

        # users are given time to post a location statement
        if not post.is_post_old(timeout_mins):
            print("\tTime has not expired")
            return
        print("\tTime has expired")

        if location_statement_state == LocationStatementState.MISSING or \
                location_statement_state == LocationStatementState.INVALID or \
                location_statement_state == LocationStatementState.INCOMPLETE:
            print(f"\tPost has {location_statement_state} location statement (source: {location_statement_source})")
            if post.is_moderator_approved():
                self.reddit_handler.report_content(post.submission,
                                                   f"Moderator approved post, but has {location_statement_state}"
                                                   f" location statement (checked: {location_statement_source}). Please look.")
            elif settings.report_location_statement_timeout:
                self.reddit_handler.report_content(post.submission,
                                                   f"Post has a {location_statement_state} location statement "
                                                   f"after timeout (checked: {location_statement_source}). Please look.")
            else:
                removal_reason = Janitor.build_removal_reason(location_statement, location_statement_state, settings)
                self.reddit_handler.remove_content(post.submission, removal_reason,
                                                   f"{location_statement_state} location statement")
        elif location_statement_state == LocationStatementState.VALID:
            # we 'save' the submission on reddit so the bot knows which posts it's already recorded
            # and 'saved' content does not need further processing
            self.reddit_handler.save_content(post.submission)
            print(f"\tPost has valid location statement (source: {location_statement_source})")
            location = Janitor.get_location_capture(location_statement)
            time_seen = Janitor.get_time_capture(location_statement)
            dt_utc = datetime.utcfromtimestamp(post.submission.created_utc)
            formatted_dt = dt_utc.isoformat().replace('T', ' ')
            sheet_values = [[location, time_seen, formatted_dt, f"https://www.reddit.com{post.submission.permalink}"]]
            self.google_sheets_recorder.append_to_sheet(subreddit.display_name, sheet_values)
        else:
            raise RuntimeError(f"\tUnsupported location_statement_state: {location_statement_state}")

    def handle_posts(self, subreddit):
        settings = self.settings_map[subreddit.display_name.lower()]
        self.handle_new_posts(subreddit, settings)


class LocationStatementState(str, Enum):
    MISSING = "MISSING"
    INVALID = "INVALID"
    INCOMPLETE = "INCOMPLETE"
    VALID = "VALID"
