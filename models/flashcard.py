class Flashcard:
    id: int
    word: str
    definition: str
    is_known: bool
    is_fav: bool
 

    def __init__(self, id, word, definition, is_known, is_fav):
        self.id = id
        self.word = word
        self.definition = definition
        self.is_known = is_known
        self.is_fav = is_fav

    def to_dict(self):
        return {
            "id": self.id,
            "word": self.word,
            "definition": self.definition,
            "is_known": self.is_known,
            "is_fav": self.is_fav,
        }

    @classmethod
    def from_dict(cls, data):
        card = cls(data["id"], data["word"], data["definition"])
        card.is_known = data.get("is_known", False)
        card.is_fav = data.get("is_fav", False)
        return card

