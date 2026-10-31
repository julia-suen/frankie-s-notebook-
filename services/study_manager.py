import random

class StudyManager:
    def __init__(self, data, storage):
        self.data = data
        self.storage = storage

    def _save(self):
        self.storage.save_data(self.data)

    def create_session(self, flashcards):
        return random.sample(flashcards, len(flashcards))

    def mark_known(self, flashcard):
        flashcard.is_known = True
        self._save()

    def mark_unknown(self, flashcard):
        flashcard.is_known = False
        self._save()

    def split_by_known(self, flashcards):
        known = [f for f in flashcards if f.is_known==True]
        unknown = [f for f in flashcards if f.is_known==False]
        return known, unknown

    def reset_known(self, flashcards):
        for f in flashcards:
            f.is_known = False
        self._save()