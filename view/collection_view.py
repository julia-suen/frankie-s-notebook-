import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class Collection(ttk.Frame):
    def __init__(self, parent, app, collection_id):
        super().__init__(parent)
        self.app = app
        self.collection_id = collection_id
        title = "All Flashcards" if collection_id is None else app.collection_manager.get_collection(collection_id).name
        ttk.Label(self, text=title, font=("Arial", 20)).pack(pady=10)
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill="both", expand=True)
        self.refresh()
        ttk.Button(self, text="+ New Flashcard", command=self.new_card).pack(pady=4)
        if collection_id is not None:
            ttk.Button(self, text="+ Add Existing", command=self.add_existing).pack(pady=4)
        ttk.Button(self, text="Study", command=lambda: app.show_study(collection_id)).pack(pady=4)
        ttk.Button(self, text="Back", command=app.show_home).pack(pady=4)

    def get_cards(self):
        if self.collection_id is None:
            return self.app.flashcard_manager.data["flashcards"]
        return self.app.collection_manager.get_collection_flashcards(self.collection_id)

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for card in self.get_cards():
            self.listbox.insert(tk.END, card.word)

    def new_card(self):
        word = simpledialog.askstring("New Flashcard", "Word:", parent=self)
        if not word:
            return
        definition = simpledialog.askstring("New Flashcard", "Definition:", parent=self)
        if not definition:
            return
        try:
            card = self.app.flashcard_manager.create_flashcard(word, definition)
            if self.collection_id is not None:
                self.app.collection_manager.add_flashcard(self.collection_id, card.id)
            self.refresh()
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def add_existing(self):
        collection = self.app.collection_manager.get_collection(self.collection_id)
        cards = [card for card in self.app.flashcard_manager.data["flashcards"]
                 if card.id not in collection.flashcard_ids]
        if not cards:
            messagebox.showinfo("Info", "No other flashcards available")
            return
        window = tk.Toplevel(self)
        window.title("Add Existing Flashcard")
        choices = tk.Listbox(window)
        choices.pack(padx=15, pady=10)
        for card in cards:
            choices.insert(tk.END, card.word)

        def add():
            if not choices.curselection():
                return
            card = cards[choices.curselection()[0]]
            self.app.collection_manager.add_flashcard(self.collection_id, card.id)
            self.refresh()
            window.destroy()

        ttk.Button(
            window,
            text="Add",
            command=add
        ).pack(pady=10)


