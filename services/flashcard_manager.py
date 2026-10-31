import storage
import models.flashcard

class FlashcardManager:
    flashcard: list
    # data_handler: storage

    # def __init__(self):
    #     self.data_handler = storage()
    #     self.flashcard = []
    #     self.load_flashcards()

    # # load flashcard from scratch every time app is restarted
    # def load_flashcards(self):
    #     pass