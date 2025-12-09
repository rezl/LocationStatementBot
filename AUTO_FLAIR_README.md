# Auto-Flair Feature

## What it does

Automatically applies "Sighting" flair to video/image posts that have Time/Location fields, so users don't have to manually flair their posts. Even if the data is incomplete, the post gets flaired and the user has 30 minutes to fix it.

## How it works

When a new post comes in without Sighting flair:

1. Check if it's a media post (video/image) → Skip if not
2. Check if domain is excluded (news sites) → Skip if yes
3. Check if post has Time/Location fields (even incomplete) → Skip if no fields at all
4. Apply "Sighting" flair
5. LocationStatementBot validates on next cycle, gives user 30 min to fix if incomplete

## Criteria

```
Auto-flair IF ALL:
  ✓ Media post (v.redd.it, i.redd.it, imgur, youtube)
  ✓ NOT a news domain
  ✓ Has Time/Location fields (even if incomplete)
```

**What happens after auto-flair:**
- VALID data → passes immediately, added to sightings database
- INCOMPLETE data → user has 30 min to fix, gets specific error message
- No fix after 30 min → removed with explanation

## Settings (settings.py)

```python
# Enable/disable auto-flair
auto_flair_enabled = True

# Dry run - logs what would be flaired without actually doing it
auto_flair_dry_run = True  # SET TO FALSE WHEN READY

# Flair text to apply
auto_flair_text = "Sighting"

# Media domains (required for auto-flair)
auto_flair_media_domains = {
    "v.redd.it", "i.redd.it", "imgur.com", ...
}

# Domains to exclude (news sites won't be auto-flaired)
auto_flair_excluded_domains = {
    "yahoo.com", "cnn.com", "bbc.com", ...
}
```

## Discord logging

Auto-flaired posts are logged to Discord:

```
Auto-flaired as **Sighting**:
**Title:** Strange lights over Phoenix
**Reason:** Incomplete data (user has 30 min to fix) - Time: 8pm, Location: Phoenix
**Link:** https://reddit.com/r/UFOs/comments/...
```

## Flow diagram

```
New post arrives (video/image)
      ↓
Has Sighting flair? ─── Yes ──→ Run location validation
      │
      No
      ↓
Auto-flair enabled? ─── No ──→ Skip
      │
      Yes
      ↓
Media post? ─── No ──→ Skip
      │
      Yes
      ↓
Excluded domain? ─── Yes ──→ Skip
      │
      No
      ↓
Has Time/Location fields? ─── No ──→ Skip (no attempt made)
      │
      Yes (even if incomplete)
      ↓
Apply "Sighting" flair
      ↓
Next cycle: Validation runs
      ↓
VALID? ──→ Pass, add to database
      │
INCOMPLETE? ──→ Wait 30 min, then remove if not fixed
```
