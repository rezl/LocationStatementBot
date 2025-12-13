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
    
    # ==========================================================================
    # Auto-flair settings
    # ==========================================================================
    
    # Enable/disable auto-flair feature
    auto_flair_enabled = True
    
    # Dry run mode - logs what would be flaired without actually flairing
    auto_flair_dry_run = False
    
    # The flair template ID to apply (from r/UFOs post flair settings)
    auto_flair_template_id = "de39d1a0-05e8-11ef-91aa-9a3acca53f53"
    
    # Domains to exclude from auto-flairing (news sites, etc.)
    auto_flair_excluded_domains = {
        # Major news sites
        "yahoo.com", "news.yahoo.com", "uk.news.yahoo.com",
        "cnn.com", "bbc.com", "bbc.co.uk",
        "nytimes.com", "washingtonpost.com",
        "theguardian.com", "reuters.com",
        "foxnews.com", "nbcnews.com", "cbsnews.com",
        "dailymail.co.uk", "nypost.com",
        "vice.com", "huffpost.com",
        "abc.com", "abcnews.go.com",
        "apnews.com", "bloomberg.com",
        "businessinsider.com", "cnbc.com",
        "forbes.com", "independent.co.uk",
        "latimes.com", "msnbc.com",
        "newsweek.com", "politico.com",
        "sky.com", "news.sky.com",
        "thehill.com", "usatoday.com", "wired.com",
        # UFO/paranormal news sites (articles, not sightings)
        "thedebrief.org", "liberationtimes.com",
        "dailygrail.com", "mysteriousuniverse.org",
        "unknowncountry.com",
        # Blogs/newsletters
        "substack.com", "open.substack.com",
        "medium.com",
        # Social media (external links)
        "twitter.com", "x.com",
        "facebook.com", "tiktok.com", "instagram.com",
        # Podcasts/video platforms (not direct uploads)
        "podcasts.apple.com", "spotify.com", "rumble.com",
    }
    
    # Domains that indicate media posts (required for auto-flair)
    auto_flair_media_domains = {
        "v.redd.it",
        "i.redd.it",
        "imgur.com",
        "i.imgur.com",
        "youtube.com",
        "youtu.be",
        "streamable.com",
        "gfycat.com",
        "drive.google.com",
    }
    
    # ==========================================================================
    
    # Base removal message template - {specific_issue} will be replaced with state-specific text
    ls_removal_reason_template = (
        "Your post has been removed because the **time** and **location** of your sighting were either missing or not in the required format.\n\n"
        "Our sightings bot requires specific formatting as outlined in the [guidelines](https://ufos.wiki/track/sightings-post-guidelines/). Note that this info must be in your post body or a comment - if it was only in the title, the bot won't detect it.\n\n"
        "{specific_issue}"
        "**Required format** (in post body or as a comment, each on a separate line):\n\n"
        "    Time: [specific date AND time of day]\n"
        "    Location: [city, state/province, country]\n\n"
        "**Note:** Your post must include the exact words `Time:` and `Location:` at the start of each line - the bot looks for these labels.\n\n"
        "❌ **Wrong:** \"I saw this on December 5th around 9pm in Phoenix, Arizona\"\n\n"
        "✅ **Right:**\n\n"
        "    Time: December 5, 2025 at 9:00 PM\n"
        "    Location: Phoenix, Arizona, USA\n\n"
        "Please provide a detailed description of your sighting (min 150 characters).\n\n"
        "To fix: If this is a text post, edit your post body. If this is a link/video/image post, add a comment with the required info. If your post has already been removed, please resubmit with the required format.\n\n"
        "**Additional sighting requirements:**\n\n"
        "- Must include a detailed and descriptive eyewitness account\n"
        "- Must have been seen with your own eyes (not found later in photos)\n"
        "- No trail camera or doorbell camera footage\n"
        "- No cell phone videos of content on a TV/display\n"
        "- Imagery must be in focus most of the time\n\n"
        "For full guidelines, see: [How to Report a Sighting](https://ufos.wiki/reports/) | [Posting Guidelines](https://reddit.com/r/UFOs/wiki/posting_guidelines) | [Investigate a Sighting](https://ufos.wiki/investigate/)\n\n"
        "This format allows your sighting to be added to the [r/UFOs Sighting Reports database](https://docs.google.com/spreadsheets/d/1Ewy0BZxaafdWulW7Vd8NQCA6u7OJ0-gCYIPeTDNgmZA/edit?usp=sharing).\n\n"
        "---\n"
        "*This is an automated message. Please [message the moderators](https://www.reddit.com/message/compose?to=/r/UFOs) if you believe this removal was made in error.*"
        "\n\n"
    )
    
    # State-specific issue descriptions
    ls_issue_missing = (
        "**Issue:** No `Time:` or `Location:` fields were found in your post.\n\n"
    )
    
    ls_issue_missing_time = (
        "**Issue:** No `Time:` field was found in your post.\n\n"
        "Your post has a `Location:` field, but the bot couldn't find a `Time:` field. "
        "Make sure you include `Time:` followed by the date and time of your sighting.\n\n"
    )
    
    ls_issue_missing_location = (
        "**Issue:** No `Location:` field was found in your post.\n\n"
        "Your post has a `Time:` field, but the bot couldn't find a `Location:` field. "
        "Make sure you include `Location:` followed by where the sighting occurred.\n\n"
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
    
    # ==========================================================================
    # Warning comment settings (posted before removal)
    # ==========================================================================
    
    # Enable/disable warning comments (if disabled, posts are removed after timeout with no prior warning)
    warning_comment_enabled = True
    
    # Warning comment template - posted when post is first detected with issues
    # {specific_issue} will be replaced with state-specific text
    ls_warning_comment_template = (
        "This post is missing the required **time** and **location** info and will be removed automatically if not added soon. If you believe you've already included this info, please check the guidelines for the correct format.\n\n"
        "Our sightings bot requires specific formatting as outlined in the [guidelines](https://ufos.wiki/track/sightings-post-guidelines/). Note that this info must be in your post body or a comment - if it was only in the title, the bot won't detect it.\n\n"
        "{specific_issue}"
        "**Required format** (in post body or as a comment, each on a separate line):\n\n"
        "    Time: [specific date AND time of day]\n"
        "    Location: [city, state/province, country]\n\n"
        "**Note:** Your post must include the exact words `Time:` and `Location:` at the start of each line - the bot looks for these labels.\n\n"
        "❌ **Wrong:** \"I saw this on December 5th around 9pm in Phoenix, Arizona\"\n\n"
        "✅ **Right:**\n\n"
        "    Time: December 5, 2025 at 9:00 PM\n"
        "    Location: Phoenix, Arizona, USA\n\n"
        "Please provide a detailed description of your sighting (min 150 characters).\n\n"
        "**How to fix:** If this is a text post, edit your post body. If this is a link/video/image post, add a comment with the required info.\n\n"
        "**Additional sighting requirements:**\n\n"
        "- Must include a detailed and descriptive eyewitness account\n"
        "- Must have been seen with your own eyes (not found later in photos)\n"
        "- No trail camera or doorbell camera footage\n"
        "- No cell phone videos of content on a TV/display\n"
        "- Imagery must be in focus most of the time\n\n"
        "For full guidelines, see: [How to Report a Sighting](https://ufos.wiki/reports/) | [Posting Guidelines](https://reddit.com/r/UFOs/wiki/posting_guidelines) | [Investigate a Sighting](https://ufos.wiki/investigate/)\n\n"
        "This format allows your sighting to be added to the [r/UFOs Sighting Reports database](https://docs.google.com/spreadsheets/d/1Ewy0BZxaafdWulW7Vd8NQCA6u7OJ0-gCYIPeTDNgmZA/edit?usp=sharing).\n\n"
        "---\n"
        "*This comment will be automatically removed once you add the required info.*"
        "\n\n"
    )

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
