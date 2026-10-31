from models.flashcard import Flashcard

class FlashcardManager:
    flashcards: list
    data: dict

    def __init__(self, data, storage):
        self.data = data
        self.storage = storage
        self.flashcards = data["flashcards"] #mutable with data in main

    def get_flashcard(self, target_card_id):
        for card in self.flashcards:
            if card.id == target_card_id:
                return card
        raise ValueError(f"No flashcard with id {target_card_id}.")

    def create_flashcard(self, word, definition):
        word = word.strip()
        definition = definition.strip()
        if not word or not definition:
            raise ValueError("Word and definition can't be empty.")

        # generate new ID
        new_id = max((card.id for card in self.flashcards), default=0) + 1

        # create new flashcard and add to shared list
        new_flashcard = Flashcard(new_id, word, definition, False, False)
        self.flashcards.append(new_flashcard)

        self.storage.save_data(self.data)

        return new_flashcard

    def toggle_favourite(self, target_card_id):
        card = self.get_flashcard(target_card_id)
        card.is_fav = not card.is_fav

        self.storage.save_data(self.data)

    def delete_flashcard(self, target_card_id):
        card = self.get_flashcard(target_card_id)
        self.flashcards.remove(card)

        # remove the card from every collection that contains it
        for collection in self.data["collections"]:
            if target_card_id in collection.flashcard_ids:
                collection.flashcard_ids.remove(target_card_id)

        self.storage.save_data(self.data)

    def edit_flashcard(self, target_card_id, new_word=None, new_definition=None):
        card = self.get_flashcard(target_card_id)

        if new_word is not None:
            new_word = new_word.strip()
            if not new_word:
                raise ValueError("Word can't be empty.")

        if new_definition is not None:
            new_definition = new_definition.strip()
            if not new_definition:
                raise ValueError("Definition can't be empty.")

        if new_word is not None:
            card.word = new_word
        if new_definition is not None:
            card.definition = new_definition

        self.storage.save_data(self.data)
