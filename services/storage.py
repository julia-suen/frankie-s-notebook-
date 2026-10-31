import json

class Storage:
    def __init__(self):
        self.file_path = "data/collections.json"
    
    def load_data(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def save_data(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


