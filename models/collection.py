class Collection:
    def __init__(self, id, name, flashcard_ids=None):
        self.id = id
        self.name = name
        self.flashcard_ids = flashcard_ids if flashcard_ids is not None else []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "flashcard_ids": self.flashcard_ids,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["flashcard_ids"])