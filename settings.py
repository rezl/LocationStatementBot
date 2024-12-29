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
    ls_removal_reason = ("Your post has been removed for not including the **time** and **location** of the sighting in the proper format.\n "
                         "You must submit your sighting post with the text **Time:** and **Location:** on separate lines like this:\n\n"
                         "\"Time: *date and time*\n\n"
                         "Location: *location of sighting*\"\n\n"
                         "This is a bot. Replies will not receive responses.\n "
                         "Please message the moderators if you feel this was an error."
                        "\n\n")

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
