import storage
from models.flashcard import Flashcard

class FlashcardManager:
    flashcards: list
    data: dict

    def __init__(self, data, storage):
        self.data = data 
        self.flashcards = data["flashcards"] #mutable with data in main 
        self.storage = storage 
        
    def create_flashcard(self, word, definition):
        # generate new ID
        new_id = max((card.id for card in self.flashcards), default=0) + 1

        # create new flashcard and add to shared list
        new_flashcard = Flashcard(new_id, word, definition, False, False)
        self.flashcards.append(new_flashcard)

        self.storage.save_data(self.data)

        return new_flashcard

    def toggle_favourite(self, target_card_id):
        for card in self.flashcards:
            if card.id == target_card_id:
                card.is_fav = not card.is_fav
                
                self.storage.save_data(self.data)
        return