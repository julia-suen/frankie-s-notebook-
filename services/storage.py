import json

from models.flashcard import Flashcard
from models.collection import Collection

class Storage:
    def __init__(self, file_path="data/collections.json"):
        self.file_path = file_path
    
    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                raw_data = json.load(file)

        except FileNotFoundError:
            raw_data = {}

        return {
            "flashcards": [Flashcard.from_dict(card) for card in raw_data.get("flashcards", [])],
            "collections": [Collection.from_dict(collection) for collection in raw_data.get("collections", [])]
        }


    def save_data(self, data):
        raw_data = {
            "flashcards": [card.to_dict() for card in data["flashcards"]],
            "collections": [collection.to_dict() for collection in data["collections"]]
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(raw_data, file, indent=4)