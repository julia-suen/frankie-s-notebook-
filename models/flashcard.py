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

    @classmethod
    def from_dict(cls, card):
        return cls(
            card["id"],
            card["word"],
            card["definition"],
            card["is_known"],
            card["is_fav"]
        )