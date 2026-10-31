from services.storage import Storage
from services.flashcard_manager import FlashcardManager
from services.collection_manager import CollectionManager
from services.study_manager import StudyManager
from view.main_view import Main


def main():
    # Initialize storage
    storage = Storage("data/collections.json")

    # Load existing data from JSON
    data = storage.load_data()

    # Initialize managers with shared data
    flashcard_manager = FlashcardManager(data, storage)
    collection_manager = CollectionManager(data, storage)
    study_manager = StudyManager(data, storage)

    app = Main(
        flashcard_manager,
        collection_manager,
        study_manager
    )
    app.mainloop()


if __name__ == "__main__":
    main()

