import json

class Storage:
    def __init__(self, file_path="data/collections.json"):
        self.file_path = file_path
        self.data = self.load_data()
    
    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
            
        except FileNotFoundError:
            return {
                "flashcards": [],
                "collections": []
            }


    def save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)


