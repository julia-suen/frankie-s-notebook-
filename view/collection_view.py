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

        edit_row = ttk.Frame(self)
        edit_row.pack(pady=4)
        ttk.Button(edit_row, text="+ New Flashcard", command=self.new_card).pack(side="left", padx=4)
        if collection_id is not None:
            ttk.Button(edit_row, text="+ Add Existing", command=self.add_existing).pack(side="left", padx=4)
        ttk.Button(edit_row, text="★ Toggle Favourite", command=self.toggle_favourite).pack(side="left", padx=4)

        study_row = ttk.Frame(self)
        study_row.pack(pady=4)
        ttk.Button(study_row, text="Study", command=lambda: app.show_study(collection_id)).pack(side="left", padx=4)
        ttk.Button(study_row, text="Study Unknown Only",
                   command=lambda: app.show_study(collection_id, True)).pack(side="left", padx=4)
        ttk.Button(study_row, text="Reset Progress", command=self.reset_progress).pack(side="left", padx=4)
        ttk.Button(study_row, text="Back", command=app.show_home).pack(side="left", padx=4)

    def get_cards(self):
        if self.collection_id is None:
            return self.app.flashcard_manager.data["flashcards"]
        return self.app.collection_manager.get_collection_flashcards(self.collection_id)

    def refresh(self):
        self.listbox.delete(0, tk.END)
        # unknown cards first, then known ones
        known, unknown = self.app.study_manager.split_by_known(self.get_cards())
        self.shown_cards = unknown + known
        for card in self.shown_cards:
            status = "✓" if card.is_known else "✗"
            star = "★ " if card.is_fav else ""
            self.listbox.insert(tk.END, f"{status}  {star}{card.word}")

    def selected_card(self):
        if not self.listbox.curselection():
            messagebox.showinfo("Info", "Select a flashcard first")
            return None
        return self.shown_cards[self.listbox.curselection()[0]]

    def toggle_favourite(self):
        card = self.selected_card()
        if card is None:
            return
        try:
            self.app.flashcard_manager.toggle_favourite(card.id)
        except ValueError as error:
            messagebox.showerror("Error", str(error))
            return
        self.refresh()
        self.listbox.selection_set(self.shown_cards.index(card))

    def reset_progress(self):
        cards = self.get_cards()
        if not cards:
            return
        if messagebox.askyesno("Reset Progress", "Mark every card here as not known?", parent=self):
            self.app.study_manager.reset_known(cards)
            self.refresh()

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