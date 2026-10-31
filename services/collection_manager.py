from models.collection import Collection


class CollectionManager:
    def __init__(self, data, storage):
        self.data = data
        self.storage = storage



    def _save(self):
        self.storage.save_data(self.data)



    def get_all_collections(self):
        return self.data["collections"]



    def get_collection(self, collection_id):
        for c in self.data["collections"]:
            if c.id == collection_id:
                return c
        raise ValueError(f"No collection with id {collection_id}.")



    def create_collection(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Collection name can't be empty.")

        for c in self.data["collections"]:
            if c.name.lower() == name.lower():
                raise ValueError(f"A collection named '{name}' already exists.")

        new_id = max((c.id for c in self.data["collections"]), default=0) + 1
        collection = Collection(new_id, name)

        self.data["collections"].append(collection)
        self._save()
        return collection



    def delete_collection(self, collection_id):
        c = self.get_collection(collection_id)
        self.data["collections"].remove(c)
        self._save()



    def add_flashcard(self, collection_id, flashcard_id):
        if not any(f.id == flashcard_id for f in self.data["flashcards"]):
            raise ValueError(f"No flashcard with id {flashcard_id}.")



        c = self.get_collection(collection_id)
        if flashcard_id not in c.flashcard_ids:
            c.flashcard_ids.append(flashcard_id)
            self._save()



    def remove_flashcard(self, collection_id, flashcard_id):
        c = self.get_collection(collection_id)
        if flashcard_id in c.flashcard_ids:
            c.flashcard_ids.remove(flashcard_id)
            self._save()



    def remove_flashcard_everywhere(self, flashcard_id):
        for c in self.data["collections"]:
            if flashcard_id in c.flashcard_ids:
                c.flashcard_ids.remove(flashcard_id)
        self._save()



    def get_collection_flashcards(self, collection_id):
        c = self.get_collection(collection_id)
        cards_by_id = {f.id: f for f in self.data["flashcards"]}
        return [cards_by_id[fid] for fid in c.flashcard_ids if fid in cards_by_id]