from services import storage
from models.collection import Collection

def get_collection(collection_id):
    for c in storage.data["collections"]:
        if c.id == collection_id:
            return c
    raise ValueError(f"No collection with id {collection_id}.")



def create_collection(name):
    name = name.strip()
    if not name:
        raise ValueError("Collection name can't be empty.")

    for c in storage.data["collections"]:
        if c.name.lower() == name.lower():
            raise ValueError(f"A collection named '{name}' already exists.")

    new_id = max((c.id for c in storage.data["collections"]), default=0) + 1
    collection = Collection(new_id, name)

    storage.data["collections"].append(collection)
    storage.save_data(storage.data)
    return collection



def delete_collection(collection_id):
    c = get_collection(collection_id)
    storage.data["collections"].remove(c)
    storage.save_data(storage.data)



def add_flashcard(collection_id, flashcard_id):
    if not any(f.id == flashcard_id for f in storage.data["flashcards"]):
        raise ValueError(f"No flashcard with id {flashcard_id}.")

    c = get_collection(collection_id)
    if flashcard_id not in c.flashcard_ids:
        c.flashcard_ids.append(flashcard_id)
        storage.save_data(storage.data)



def remove_flashcard(collection_id, flashcard_id):
    
    c = get_collection(collection_id)
    for f in range(len(c.flashcard_ids)):
        if c.flashcard_ids[f] == flashcard_id:
            del c.flashcard_ids[f]
            break
    storage.save_data(storage.data)



def remove_flashcard_everywhere(flashcard_id):
    for c in storage.data["collections"]:
        remove_flashcard(c.id, flashcard_id)
    storage.save_data(storage.data)



def get_collection_flashcards(collection_id):
    c = get_collection(collection_id)
    cards_by_id = {f.id: f for f in storage.data["flashcards"]}
    return [cards_by_id[fid] for fid in c.flashcard_ids if fid in cards_by_id]