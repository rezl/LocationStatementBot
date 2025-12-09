# LocationStatementBot - Sighting Post Validation

## Overview

This bot enforces sighting post requirements on r/UFOs by:
1. **Auto-flairing** media posts that have Time/Location fields
2. **Validating** that Sighting posts have proper Time and Location info
3. **Warning** users with a pinned comment if info is missing/incomplete
4. **Removing** posts that aren't fixed within 30 minutes

---

## Full Logic Flow

```
Every 5 minutes, bot checks posts up to 2 hours old:

FOR EACH POST
     │
     ▼
┌─────────────────────────────┐
│ Has Sighting flair already? │
└─────────────────────────────┘
         │            │
        NO           YES
         │            │
         ▼            │
┌─────────────────┐   │
│ AUTO-FLAIR      │   │
│ CHECKS:         │   │
│                 │   │
│ • Media post?   │   │
│ • Not news?     │   │
│ • Has fields?   │   │
└─────────────────┘   │
    │         │       │
  FAIL      PASS      │
    │         │       │
    ▼         ▼       │
  SKIP    Apply       │
          Sighting    │
          flair       │
            │         │
            └────┬────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              VALIDATE LOCATION STATEMENT                │
│                                                         │
│  Check in order (keep best state found):                │
│    1. Post body                                         │
│    2. OP comments (with "location" keyword)             │
│    3. Title                                             │
│                                                         │
│  Accepts formats like:                                  │
│    • Time: Dec 9, 2025 8pm  (with colon)                │
│    • Time Dec 9, 2025 8pm   (without colon)             │
│    • Date: Dec 9 Location: Phoenix                      │
│                                                         │
│  Returns:                                               │
│    VALID      = Has date + time-of-day + location       │
│    INCOMPLETE = Missing date OR time-of-day             │
│    INVALID    = Fields found but empty                  │
│    MISSING    = No Time:/Location: fields at all        │
└─────────────────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────┐
│       VALID?                │
└─────────────────────────────┘
         │            │
        YES          NO
         │            │
         ▼            ▼
┌──────────────┐  ┌─────────────────────────────┐
│ Delete any   │  │ Warning comment on post?    │
│ old warning  │  └─────────────────────────────┘
│ comment      │           │            │
└──────────────┘          NO           YES
         │                 │            │
         ▼                 ▼            ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Save post    │  │ Post older   │  │ Post older   │
│ Log to       │  │ than 30 min? │  │ than 30 min? │
│ Google       │  └──────────────┘  └──────────────┘
│ Sheets       │       │      │          │      │
└──────────────┘      NO     YES        NO     YES
                       │      │          │      │
                       ▼      │          ▼      │
                 ┌──────────┐ │    ┌──────────┐ │
                 │ POST     │ │    │   WAIT   │ │
                 │ WARNING  │ │    │  (next   │ │
                 │ COMMENT  │ │    │  cycle)  │ │
                 │ (pinned) │ │    └──────────┘ │
                 └──────────┘ │                 │
                       │      └────────┬────────┘
                       ▼               │
                     DONE              ▼
                            ┌─────────────────────┐
                            │ Delete warning      │
                            │ comment             │
                            └─────────────────────┘
                                       │
                                       ▼
                            ┌─────────────────────┐
                            │ Mod-approved?       │
                            └─────────────────────┘
                                  │         │
                                 YES       NO
                                  │         │
                                  ▼         ▼
                            ┌─────────┐ ┌─────────┐
                            │ REPORT  │ │ REMOVE  │
                            │ to mods │ │ post +  │
                            │         │ │ removal │
                            └─────────┘ │ comment │
                                        └─────────┘
```

---

## Validation States

| State | Meaning | Example | Action |
|-------|---------|---------|--------|
| **VALID** | Has date + time-of-day + location | `Time: Dec 9, 2025 8pm Location: Phoenix` | ✅ Save to database |
| **INCOMPLETE** | Missing date OR time-of-day | `Time: 8pm Location: Phoenix` (no date) | ⚠️ Warning → Remove |
| **INVALID** | Fields found but empty | `Time: Location:` | ⚠️ Warning → Remove |
| **MISSING** | No Time:/Location: fields | Just a description with no fields | ⚠️ Warning → Remove |

---

## Warning Comment

When a post has issues, a **pinned comment** is posted immediately:

> This post needs the required **time** and **location** info or it will be removed.
>
> **Issue:** [specific issue - e.g., "Missing specific date"]
>
> **Required format** (in post body or as a comment, each on a separate line):
>
> > Time: [specific date AND time of day]
> >
> > Location: [city, state/province, country]
>
> **Example:**
>
> > Time: December 9, 2025 at 10:30 PM
> >
> > Location: Phoenix, Arizona, USA
>
> *This comment will be automatically removed once you add the required info.*

**If user fixes their post:** Warning comment is deleted, post is saved to database.

**If user doesn't fix within 30 min:** Warning deleted, post removed with removal comment.

---

## Issue-Specific Messages

| Issue | Warning Message |
|-------|-----------------|
| **MISSING** | "No `Time:` or `Location:` fields were found in your post." |
| **INVALID** | "The `Time:` or `Location:` fields were found but appear to be empty." |
| **Missing date** | "Your time field is missing a **specific date**. Please include an actual date like `December 7th` or `12/7/24`" |
| **Missing time** | "Your time field is missing the **time of day**. Please add a time like `8pm`, `20:00`, or even `evening`" |
| **Missing both** | "Your time field is missing both a **specific date** and **time of day**." |

---

## Auto-Flair Feature

Automatically applies "Sighting" flair to media posts that have Time/Location fields.

### Criteria

```
Auto-flair IF ALL:
  ✓ Media post (v.redd.it, i.redd.it, imgur, youtube, galleries)
  ✓ NOT a news domain (yahoo, cnn, bbc, etc.)
  ✓ Has Time/Location fields (even if incomplete)
```

### Settings

```python
# Enable/disable auto-flair
auto_flair_enabled = True

# Dry run mode - logs without actually flairing
auto_flair_dry_run = False

# Flair template ID (from subreddit settings)
auto_flair_template_id = "de39d1a0-05e8-11ef-91aa-9a3acca53f53"

# Media domains that trigger auto-flair
auto_flair_media_domains = {
    "v.redd.it", "i.redd.it", "imgur.com", "youtube.com", ...
}

# Excluded domains (news sites)
auto_flair_excluded_domains = {
    "yahoo.com", "cnn.com", "bbc.com", "nytimes.com", ...
}
```

---

## Configuration (settings.py)

```python
# How often bot checks (minutes)
post_check_frequency_mins = 5

# How far back to check posts (minutes)
post_check_threshold_mins = 120  # 2 hours

# Time before removal (minutes)
location_statement_time_limit_mins = 30

# Flairs that trigger validation
sightings_flair = ["Sighting"]

# Report instead of remove?
report_location_statement_timeout = False

# Dry run mode (no actions taken)
is_dry_run = False
```

---

## Files

| File | Purpose |
|------|---------|
| `janitor.py` | Main validation logic, auto-flair, warning comments |
| `settings.py` | All configuration and message templates |
| `discord_client.py` | Discord logging for actions and errors |
| `bot.py` | Main loop, Reddit connection |
| `post.py` | Post wrapper class |
| `reddit_actions_handler.py` | Remove, report, reply actions |
| `google_sheets_recorder.py` | Logs valid sightings to Google Sheets |

---

## Discord Logging

Actions are logged to Discord:

```
Posted warning comment on post:
**Post:** Strange lights over Phoenix...
**Issue:** INCOMPLETE
**Link:** https://reddit.com/r/UFOs/comments/...
```

```
User fixed their post, deleted warning comment:
**Post:** Strange lights over Phoenix...
**Link:** https://reddit.com/r/UFOs/comments/...
```

```
Auto-flaired as **Sighting**:
**Title:** UFO over my house
**Reason:** Valid data - Time: Dec 9 8pm, Location: Phoenix
**Link:** https://reddit.com/r/UFOs/comments/...
```
