"""TODO: Module Description Here"""

import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    """TODO"""
    def __init__(self) -> None:
        super().__init__()

        self.title("Frankie's Notebook")
        self.geometry("800x600")
        self.minsize(400, 300)

        # Dummy data for now TODO: replace this later
        self.flashcards = [
            {
                "id": 1,
                "word": "apple",
                "definition": "It doesn't fall from its tree.",
                "is_known": False,
                "is_fav": False
            },
            {
                "id": 2,
                "word": "banana",
                "definition": "Monkeys love this one!",
                "is_known": False,
                "is_fav": True
            },
            {
                "id": 3,
                "word": "Emma",
                "definition": "She is lactose intolerant",
                "is_known": True,
                "is_fav": False
            }
        ]

        self.collections = [
            {
                "id": 1,
                "name": "Fruits",
                "flashcard_ids": [1, 2]
            },
            {
                "id": 2,
                "name": "Names",
                "flashcard_ids": [3]
            }
        ]

        self.container = ttk.Frame(self, padding=20)
        self.container.pack(fill="both", expand=True)

        self.show_home()

        # TODO: clear_screen, show_home, show_collection, show_study
        def clear_screen(self):
            for widget in self.container.winfo_children():
                widget.destroy()

        def show_home(self):
            # TODO

        def show_collection(self):
            # TODO

        def show_study(self):
            # TODO



        ttk.Label(self, text="HELLO THIS IS A TEST").pack(padx=20, pady=20) # TODO: remove this later


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['tkinter'],  # the names (strs) of imported modules
    #     'allowed-io': [],  # the names (strs) of functions that call print/open/input
    #     'max-line-length': 120
    # })

    app = App()
    app.mainloop()
    # TODO: app.run()
