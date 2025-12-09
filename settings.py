import re


class Settings:
    # is_dry_run and post_check_frequency_mins should not be overridden
    # set to True to prevent any bot actions (report, remove, comments)
    is_dry_run = False
    post_check_frequency_mins = 5

    report_location_statement_timeout = False

    post_check_threshold_mins = 2 * 60
    consecutive_old_posts = 5

    location_statement_time_limit_mins = 30

    sightings_flair = ["Sighting"]
    
    # Base removal message template - {specific_issue} will be replaced with state-specific text
    ls_removal_reason_template = (
        "Your post has been removed because the **time** and **location** of your sighting were not included in the required format.\n\n"
        "{specific_issue}"
        "You must include both fields in your post **title**, **body**, or **comment** using this format:\n\n"
        ">Time: [specific date AND time of day]\n>\n"
        ">Location: [city, state/province, country]\n\n"
        "**Example:**\n\n"
        ">Time: December 9, 2025 at 10:30 PM\n>\n"
        ">Location: Phoenix, Arizona, USA\n\n"
        "This format allows your sighting to be added to the [r/UFOs Sighting Reports database](https://docs.google.com/spreadsheets/d/1Ewy0BZxaafdWulW7Vd8NQCA6u7OJ0-gCYIPeTDNgmZA/edit?usp=sharing).\n\n"
        "Please resubmit your post with the required format.\n\n"
        "---\n"
        "*This is an automated message. Please [message the moderators](https://www.reddit.com/message/compose?to=/r/UFOs) if you believe this removal was made in error.*"
        "\n\n"
    )
    
    # State-specific issue descriptions
    ls_issue_missing = (
        "**Issue:** No `Time:` or `Location:` fields were found in your post.\n\n"
    )
    
    ls_issue_invalid = (
        "**Issue:** The `Time:` or `Location:` fields were found but appear to be empty.\n\n"
    )
    
    ls_issue_incomplete_no_date = (
        "**Issue:** Your time field is missing a **specific date**.\n\n"
        "You wrote a time of day but didn't include when it happened. "
        "Please include an actual date like `December 7th` or `12/7/24` - "
        "relative terms like `yesterday` or `Saturday` don't work because they become meaningless over time.\n\n"
    )
    
    ls_issue_incomplete_no_time = (
        "**Issue:** Your time field is missing the **time of day**.\n\n"
        "You included a date but didn't specify what time it happened. "
        "Please add a time like `8pm`, `20:00`, or even `evening` or `night`.\n\n"
    )
    
    ls_issue_incomplete_neither = (
        "**Issue:** Your time field is missing both a **specific date** and **time of day**.\n\n"
        "Please include when the sighting happened, for example: `December 7, 2024 at 8pm`\n\n"
    )
    
    # Fallback for backwards compatibility
    ls_removal_reason = ls_removal_reason_template.format(specific_issue="")

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
