from tkinter import ttk


class Study(ttk.Frame):
    def __init__(self, parent, app, collection_id):
        super().__init__(parent)
        self.app = app
        self.collection_id = collection_id
        cards = (app.flashcard_manager.data["flashcards"] if collection_id is None
                 else app.collection_manager.get_collection_flashcards(collection_id))
        self.cards = app.study_manager.create_session(cards)
        self.index = 0
        self.word = ttk.Label(self, font=("Arial", 24))
        self.word.pack(pady=25)
        self.definition = ttk.Label(self, wraplength=500)
        self.definition.pack(pady=15)
        ttk.Button(self, text="Reveal", command=self.reveal).pack(pady=5)
        ttk.Button(self, text="I Know", command=lambda: self.mark(True)).pack(pady=5)
        ttk.Button(self, text="I Don't Know", command=lambda: self.mark(False)).pack(pady=5)
        ttk.Button(self, text="Back", command=lambda: app.show_collection(collection_id)).pack(pady=10)
        self.show_card()

    def show_card(self):
        self.definition.config(text="")
        self.word.config(text=self.cards[self.index].word if self.index < len(self.cards)
                         else "Finished!")

    def reveal(self):
        if self.index < len(self.cards):
            self.definition.config(text=self.cards[self.index].definition)

    def mark(self, known):
        if self.index >= len(self.cards):
            return
        card = self.cards[self.index]
        if known:
            self.app.study_manager.mark_known(card)
        else:
            self.app.study_manager.mark_unknown(card)
        self.index += 1
        self.show_card()
