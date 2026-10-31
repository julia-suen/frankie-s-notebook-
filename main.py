from services.storage import Storage
from models import Flashcard
from models import Collection
from services import FlashcardManager
from services import CollectionManager
from services import StudyManager


def main():

    # Initialize storage
    storage = Storage("data/collections.json")

    # Load existing data from JSON
    data = storage.load_data()

    # Initialize managers with shared data
    flashcard_manager = FlashcardManager(data, storage)
    collection_manager = CollectionManager(data, storage)
    study_manager = StudyManager(data, storage)

    


if __name__ == "__main__":
    main()