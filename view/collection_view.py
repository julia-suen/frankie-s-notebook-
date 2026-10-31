"""TODO: Module Description Here"""

import tkinter as tk
from tkinter import ttk, messagebox


class Collection(ttk.Frame):
    """TODO"""
    def __init__(self, parent, app, collection_id) -> None:
        super().__init__(parent)

        self.app = app
        self.collection_id = collection_id

        self.create_ui()

    def get_collection(self):
        """TODO"""
        for collection in self.app.collections:
            if collection["id"] == self.collection_id:
                return collection
        return None

    def get_flashcards(self):
        """TODO"""
        if self.collection_id is None:
            return self.app.flashcards  # return all flashcards

        collection = self.get_collection()

        if collection is None:
            return []

        ids = collection["flashcard_ids"]

        return [
            card for card in self.app.flashcards
            if card["id"] in ids
        ]

    def create_ui(self):
        """TODO"""
        collection = self.get_collection()

        title = (
            "All Flashcards"
            if self.collection_id is None
            else collection["name"] if collection
            else "Collection Not Found"    # TODO: is this necessary???
        )

        ttk.Label(
            self,
            text=title,
            font=("Comic Sans MS", 20, "bold")
        ).pack(pady=15)

        # Display the flashcards
        self.card_list = tk.Listbox(self, height=12)
        self.card_list.pack(fill="both", expand=True, pady=10)

        self.refresh_list()

        ttk.Button(
            self,
            text="Add Flashcard",
            command=self.add_flashcard_dialog
        ).pack(pady=5)

        ttk.Button(
            self,
            text="Start Studying",
            command=lambda: self.app.show_study(
                self.collection_id
            )
        ).pack(pady=5)

        ttk.Button(
            self,
            text="Back",
            command=self.app.show_home
        ).pack(pady=5)

    def refresh_list(self):
        self.card_list.delete(0, tk.END)

        for card in self.get_flashcards():
            self.card_list.insert(tk.END, card["word"])

    def add_flashcard_dialog(self):
        dialog = tk.Toplevel(self)
        dialog.title("Add Flashcard")
        dialog.geometry("350x250")  # TODO
        dialog.transient(self.winfo_toplevel())
        dialog.grab_set()

        ttk.Label(dialog, text="Word").pack(pady=5)
        word_entry = ttk.Entry(dialog)
        word_entry.pack(fill="x", padx=20)

        ttk.Label(dialog, text="Definition").pack(pady=5)
        definition_entry = ttk.Entry(dialog)
        definition_entry.pack(fill="x", padx=20)

        def save_flashcard():
            word = word_entry.get().strip()
            definition = definition_entry.get().strip()

            if not word or not definition:
                messagebox.showwarning(
                    "Missing information",
                    "Please enter a word and definition.",
                    parent=dialog
                )
                return

            new_id = max(
                (card["id"] for card in self.app.flashcards),
                default=0
            ) + 1

            new_card = {
                "id": new_id,
                "word": word,
                "definition": definition,
                "is_known": False
            }

            # Always add to master list
            self.app.flashcards.append(new_card)

            # Also add to the selected collection
            if self.collection_id is not None:
                collection = self.get_collection()
                if collection is not None:
                    collection["flashcard_ids"].append(new_id)

            self.refresh_list()
            dialog.destroy()

        ttk.Button(
            dialog,
            text="Save",
            command=save_flashcard
        ).pack(pady=15)

