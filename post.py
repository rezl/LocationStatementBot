from datetime import datetime, timedelta


class Post:
    def __init__(self, submission):
        self.submission = submission
        self.created_time = datetime.utcfromtimestamp(submission.created_utc)

    def __str__(self):
        return f"{self.submission.permalink} | {self.submission.title}"

    def has_sightings_flair(self, settings):
        flair = self.submission.link_flair_text
        if not flair:
            return False
        if flair.lower() in settings.sightings_flair:
            return True
        return False

    def is_post_old(self, time_mins):
        return self.created_time + timedelta(minutes=time_mins) < datetime.utcnow()

    def find_location_statement(self):
        candidates = []
        for comment in self.submission.comments:
            if comment.is_submitter:
                candidates.append(comment)

        if len(candidates) == 0:
            return None

        for candidate in candidates:
            text = candidate.body.lower()
            if "location" in text:
                return candidate
        return None

    def is_moderator_approved(self):
        return self.submission.approved
