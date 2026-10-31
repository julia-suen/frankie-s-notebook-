class Collection:
    def __init__(self, id, name, flashcard_ids=None):
        self.id = id
        self.name = name
        self.flashcard_ids = flashcard_ids if flashcard_ids is not None else []