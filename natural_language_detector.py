"""
Natural Language Detector for Location Statement Bot.

Tier 2 detection: Finds date, time, and location information buried in
natural language prose when users don't use the strict Time:/Location: format.
"""

import re
from dataclasses import dataclass
from typing import Optional, List

from location_data import (
    ALL_LOCATIONS, ALL_ABBREVIATIONS, ALL_REGIONS, ALL_CITIES,
    LOCATION_INDICATORS
)


@dataclass
class DetectionResult:
    """Result of natural language detection."""
    date: Optional[str] = None
    time: Optional[str] = None
    location: Optional[str] = None
    is_valid: bool = False

    # Track which sources contributed to the detection
    date_source: Optional[str] = None  # 'title', 'body', 'comment'
    time_source: Optional[str] = None
    location_source: Optional[str] = None


def get_combined_text(post) -> str:
    """
    Aggregate text from post title, body, and OP's comments.

    Args:
        post: A Post object wrapping a Reddit submission

    Returns:
        Combined text from all sources, newline-separated
    """
    parts = []

    # Title
    if post.submission.title:
        parts.append(post.submission.title)

    # Body (selftext)
    if post.submission.selftext:
        parts.append(post.submission.selftext)

    # OP's comments
    try:
        post.submission.comments.replace_more(limit=0)
        for comment in post.submission.comments:
            if comment.is_submitter and hasattr(comment, 'body'):
                parts.append(comment.body)
    except Exception:
        # If we can't load comments, continue with what we have
        pass

    return "\n".join(parts)


def get_combined_text_with_sources(post) -> List[tuple]:
    """
    Get text from each source separately for tracking.

    Returns:
        List of (text, source_name) tuples
    """
    sources = []

    if post.submission.title:
        sources.append((post.submission.title, 'title'))

    if post.submission.selftext:
        sources.append((post.submission.selftext, 'body'))

    try:
        post.submission.comments.replace_more(limit=0)
        for comment in post.submission.comments:
            if comment.is_submitter and hasattr(comment, 'body'):
                sources.append((comment.body, 'comment'))
    except Exception:
        pass

    return sources


# =============================================================================
# DATE DETECTION
# =============================================================================

# Patterns for specific dates (reused from janitor.py, extended)
DATE_PATTERNS = [
    # Full date formats
    (r'(\d{1,2}[/\-\.]\d{1,2}[/\-\.]\d{2,4})', 'numeric'),  # 12/7/24, 12-7-2024

    # Month name + day + optional year
    (r'((?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}(?:st|nd|rd|th)?(?:\s*,?\s*\d{4})?)', 'month_first'),
    (r'((?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)\.?\s+\d{1,2}(?:st|nd|rd|th)?(?:\s*,?\s*\d{4})?)', 'month_abbrev_first'),

    # Day + month name + optional year
    (r'(\d{1,2}(?:st|nd|rd|th)?\s+(?:of\s+)?(?:january|february|march|april|may|june|july|august|september|october|november|december)(?:\s*,?\s*\d{4})?)', 'day_first'),
    (r'(\d{1,2}(?:st|nd|rd|th)?\s+(?:of\s+)?(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)\.?(?:\s*,?\s*\d{4})?)', 'day_abbrev_first'),

    # German/European format: 15. Januar 2025 or 15. Jan 2025
    (r'(\d{1,2}\.\s*(?:januar|februar|marz|märz|april|mai|juni|juli|august|september|oktober|november|dezember)(?:\s+\d{4})?)', 'german_full'),
    (r'(\d{1,2}\.\s*(?:jan|feb|mar|mär|apr|mai|jun|jul|aug|sep|okt|nov|dez)\.?(?:\s+\d{4})?)', 'german_abbrev'),

    # Partial date (month/day without year)
    (r'(\d{1,2}[/\-\.]\d{1,2})(?![/\-\.]\d)', 'partial_numeric'),
]


def detect_date(text: str) -> Optional[str]:
    """
    Extract a specific date from natural language text.

    Args:
        text: The text to search

    Returns:
        The matched date string, or None if no date found
    """
    if not text:
        return None

    text_lower = text.lower()

    for pattern, _ in DATE_PATTERNS:
        match = re.search(pattern, text_lower, re.IGNORECASE)
        if match:
            # Return the original case version
            start, end = match.span()
            # Find this position in original text
            original_match = re.search(pattern, text, re.IGNORECASE)
            if original_match:
                return original_match.group(1).strip()
            return match.group(1).strip()

    return None


# =============================================================================
# TIME DETECTION
# =============================================================================

TIME_PATTERNS = [
    # HH:MM formats (highest priority - unambiguous)
    (r'(\d{1,2}:\d{2}(?:\s*(?:am|pm|a\.m\.|p\.m\.))?)', 'colon'),

    # Hour + am/pm (unambiguous)
    (r'(\d{1,2}\s*(?:am|pm|a\.m\.|p\.m\.))', 'hour_ampm'),

    # Descriptive times (unambiguous)
    (r'\b(morning|afternoon|evening|night|midnight|noon|dusk|dawn)\b', 'descriptive'),

    # "around X" (but not dates like "around 8th")
    # Negative lookahead ensures we don't match partial numbers (around 15th shouldn't match "around 1")
    (r'around\s+(\d{1,2})(?!\d)(?:\s*(?:am|pm|a\.m\.|p\.m\.|o\'?clock))?(?!(?:th|st|nd|rd)\b)', 'around'),

    # Military time (4 digits, 0000-2359) - EXCLUDING years
    # Must not be preceded by comma+space (date context) or be a year (19xx, 20xx pattern after month)
    # Only match if it looks like intentional military time, not a year
    (r'(?<![,\s\d])((?:0\d|1\d|2[0-3])[0-5]\d)(?!\d)', 'military'),
]


def _is_likely_year(text: str, match_start: int, match_value: str) -> bool:
    """Check if a 4-digit number is likely a year rather than military time."""
    # Years typically start with 19 or 20
    if match_value.startswith('19') or match_value.startswith('20'):
        # Check if preceded by month name or comma (date context)
        prefix = text[:match_start].lower()
        month_names = ['january', 'february', 'march', 'april', 'may', 'june',
                       'july', 'august', 'september', 'october', 'november', 'december',
                       'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug', 'sep', 'sept', 'oct', 'nov', 'dec']
        for month in month_names:
            if prefix.rstrip().endswith(month) or prefix.rstrip().endswith(month + ','):
                return True
        # Check if preceded by comma and space (like "December 10, 2025")
        if prefix.rstrip().endswith(','):
            return True
        # Check if preceded by a day number (like "10, 2025" or "10th 2025")
        if re.search(r'\d{1,2}(?:st|nd|rd|th)?\s*,?\s*$', prefix):
            return True
        # Check if preceded by slash or dash (numeric date format like "1/15/2025" or "1-15-2025")
        if prefix.rstrip().endswith('/') or prefix.rstrip().endswith('-'):
            return True
        # Check for full numeric date pattern before (like "1/15/")
        if re.search(r'\d{1,2}[/\-]\d{1,2}[/\-]$', prefix):
            return True
    return False


def detect_time(text: str) -> Optional[str]:
    """
    Extract a time-of-day from natural language text.

    Args:
        text: The text to search

    Returns:
        The matched time string, or None if no time found
    """
    if not text:
        return None

    for pattern, pattern_type in TIME_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            result = match.group(1).strip() if match.lastindex else match.group(0).strip()

            # For military time pattern, check if it's actually a year
            if pattern_type == 'military':
                if _is_likely_year(text, match.start(), result):
                    continue  # Skip this match, try next pattern

            # For "around X" pattern, include the "around" prefix for clarity
            if pattern_type == 'around':
                full_match = match.group(0).strip()
                return full_match

            return result

    return None


# =============================================================================
# LOCATION DETECTION
# =============================================================================

def detect_location(text: str) -> Optional[str]:
    """
    Extract a location from natural language text.

    Uses multiple strategies:
    1. Pattern matching: "[Word], [State/Country abbreviation]"
    2. Indicator phrases: "in/near/close to [Place]"
    3. Database lookup: Known cities, states, countries

    Args:
        text: The text to search

    Returns:
        The matched location string, or None if no location found
    """
    if not text:
        return None

    # Strategy 1: "[Word(s)], [Abbreviation]" pattern (highest confidence)
    # Matches: "Milford, NJ", "Milford,NJ", "New York, NY"
    abbrev_pattern = r'([A-Za-z][A-Za-z\s\.\-\']+?)\s*,\s*([A-Z]{2,3})\b'
    match = re.search(abbrev_pattern, text)
    if match:
        potential_abbrev = match.group(2).lower()
        if potential_abbrev in ALL_ABBREVIATIONS:
            return f"{match.group(1).strip()}, {match.group(2)}"

    # Strategy 2: "[Word(s)], [State/Country name]" pattern
    # Matches: "Sydney, Australia", "London, England"
    for region in sorted(ALL_REGIONS, key=len, reverse=True):  # Check longer names first
        # Build pattern for "City, Region"
        pattern = rf'([A-Za-z][A-Za-z\s\.\-\']+?)\s*,\s*({re.escape(region)})\b'
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return f"{match.group(1).strip()}, {match.group(2)}"

    # Strategy 3: Indicator phrase + location
    # Matches: "close to Phoenix", "in London", "near the UK"
    text_lower = text.lower()

    for indicator in LOCATION_INDICATORS:
        # Build pattern for indicator + potential location
        # Allow for articles: "in the UK", "near the coast"
        pattern = rf'\b{re.escape(indicator)}\s+(?:the\s+)?([A-Za-z][A-Za-z\s\.\-\']*)'

        for match in re.finditer(pattern, text_lower):
            potential_location = match.group(1).strip()

            # Clean up: remove trailing common words that aren't locations
            potential_location = re.sub(r'\s+(and|or|but|when|where|which|that|this|the|a|an).*$', '', potential_location, flags=re.IGNORECASE)
            potential_location = potential_location.strip(' .,;:')

            if not potential_location:
                continue

            # Check if it's a known location
            potential_lower = potential_location.lower()

            # Check against our database
            if potential_lower in ALL_LOCATIONS:
                # Return with original capitalization from text
                original_match = re.search(rf'\b{re.escape(indicator)}\s+(?:the\s+)?({re.escape(potential_location)})', text, re.IGNORECASE)
                if original_match:
                    return original_match.group(1).strip()
                return potential_location

            # Check if any word in the potential location is a known place
            words = potential_location.split()
            for i in range(len(words), 0, -1):
                partial = ' '.join(words[:i]).lower()
                if partial in ALL_LOCATIONS:
                    original = ' '.join(words[:i])
                    return original

    # Strategy 4: Standalone known location (lowest confidence)
    # Only check for unambiguous locations (cities are fairly unambiguous)
    for city in sorted(ALL_CITIES, key=len, reverse=True):
        # Use word boundaries to avoid partial matches
        pattern = rf'\b{re.escape(city)}\b'
        match = re.search(pattern, text_lower)
        if match:
            # Get original capitalization
            original_match = re.search(pattern, text, re.IGNORECASE)
            if original_match:
                return original_match.group(0)
            return city.title()

    # Also check regions/countries as standalone (states, countries)
    for region in sorted(ALL_REGIONS, key=len, reverse=True):
        if len(region) < 4:  # Skip very short abbreviations to avoid false positives
            continue
        pattern = rf'\b{re.escape(region)}\b'
        match = re.search(pattern, text_lower)
        if match:
            original_match = re.search(pattern, text, re.IGNORECASE)
            if original_match:
                return original_match.group(0)
            return region.title()

    return None


# =============================================================================
# COMBINED DETECTION
# =============================================================================

def detect_all(text: str) -> DetectionResult:
    """
    Run all detection methods on the given text.

    Args:
        text: The text to analyze

    Returns:
        DetectionResult with date, time, location, and validity
    """
    result = DetectionResult()

    result.date = detect_date(text)
    result.time = detect_time(text)
    result.location = detect_location(text)

    # Valid if all three components are present
    result.is_valid = all([result.date, result.time, result.location])

    return result


def detect_all_from_post(post) -> DetectionResult:
    """
    Run detection on all text sources from a post (title, body, comments).
    Aggregates results from all sources.

    Args:
        post: A Post object wrapping a Reddit submission

    Returns:
        DetectionResult with the best matches from all sources
    """
    result = DetectionResult()

    sources = get_combined_text_with_sources(post)

    for text, source_name in sources:
        # Try to find date if we don't have one yet
        if not result.date:
            date = detect_date(text)
            if date:
                result.date = date
                result.date_source = source_name

        # Try to find time if we don't have one yet
        if not result.time:
            time = detect_time(text)
            if time:
                result.time = time
                result.time_source = source_name

        # Try to find location if we don't have one yet
        if not result.location:
            location = detect_location(text)
            if location:
                result.location = location
                result.location_source = source_name

        # If we have all three, we're done
        if result.date and result.time and result.location:
            break

    # Valid if all three components are present
    result.is_valid = all([result.date, result.time, result.location])

    return result


def detect_all_combined(post) -> DetectionResult:
    """
    Alternative detection that combines all text first, then searches.
    May find patterns that span multiple sources.

    Args:
        post: A Post object wrapping a Reddit submission

    Returns:
        DetectionResult from combined text analysis
    """
    combined_text = get_combined_text(post)
    result = detect_all(combined_text)

    # Mark sources as 'combined' since we don't track individual sources here
    if result.date:
        result.date_source = 'combined'
    if result.time:
        result.time_source = 'combined'
    if result.location:
        result.location_source = 'combined'

    return result
