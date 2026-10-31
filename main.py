from services import Storage
from models import Flashcard
from models import Collection
from services import FlashcardManager
from services import CollectionManager


def main():

    # Initialize storage
    storage = Storage("data/collections.json")

    # Load existing data from JSON
    raw_data = storage.load_data()

    # initialize empty data dictionary
    data = {
        "flashcards": [], "collections": []
    }

    # Convert raw dictionaries into Python objects
    for card in raw_data["flashcards"]:
        flashcard = Flashcard.from_dict(card)
        data["flashcards"].append(flashcard)

    for collection in raw_data["collections"]:
        Collection.from_dict(collection)

    # Initialize managers with shared data
    flashcard_manager = FlashcardManager(data)
    collection_manager = CollectionManager(data)

    


if __name__ == "__main__":
    main()