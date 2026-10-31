class Flashcard:
    id: int
    word: str
    definition: str
    is_known: bool
    is_fav: bool
 

    def __init__(self, id, word, definition):
        self.id = id
        self.word = word
        self.definition = definition
        self.is_known = False
        self.is_fav = False

