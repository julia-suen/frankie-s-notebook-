# """TODO: Module Description Here"""
#
# import tkinter as tk
# from tkinter import ttk, simpledialog, messagebox
#
# from view.collection_view import Collection # TODO
# # from view.study_view import Study # TODO
#
# class Main(tk.Tk):
#     """TODO"""
#     def __init__(self) -> None:
#         super().__init__()
#
#         self.title("Frankie's Notebook")
#         self.geometry("800x600")
#         self.minsize(400, 300)
#
#         self.flashcard_manager = flashcard_manager
#         self.collection_manager = collection_manager
#         self.study_manager = study_manager
#
#         self.container = ttk.Frame(self, padding=20)
#         self.container.pack(fill="both", expand=True)
#
#         self.show_home()
#
#     def show_screen(self, screen, *args):
#         for widget in self.container.winfo_children():
#             widget.destroy()
#         screen(self.container, self, *args).pack(fill="both", expand=True)
#
#     def show_home(self):
#         for widget in self.container.winfo_children():
#             widget.destroy()
#         ttk.Label(self.container, text="My Library", font=("Arial", 22)).pack(pady=15)
#         ttk.Button(self.container, text="All Flashcards",
#                    command=lambda: self.show_collection(None)).pack(pady=5)
#         for collection in self.collection_manager.get_all_collections():
#             ttk.Button(self.container, text=collection.name,
#                        command=lambda cid=collection.id: self.show_collection(cid)).pack(pady=5)
#         ttk.Button(self.container, text="+ New Collection",
#                    command=self.new_collection).pack(pady=15)
#
#     def new_collection(self):
#         name = simpledialog.askstring("New Collection", "Collection name:", parent=self)
#         if not name:
#             return
#         try:
#             self.collection_manager.create_collection(name)
#             self.show_home()
#         except ValueError as error:
#             messagebox.showerror("Error", str(error))
#
#     def show_collection(self, collection_id=None):
#         self.show_screen(Collection, collection_id)
#
#     def show_study(self, collection_id=None):
#         self.show_screen(Study, collection_id)

import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from view.collection_view import Collection
from view.study_view import Study


class Main(tk.Tk):
    def __init__(self, flashcard_manager=None, collection_manager=None, study_manager=None):
        super().__init__()
        self.title("Frankie's Notebook")
        self.geometry("700x500")
        self.flashcard_manager = flashcard_manager
        self.collection_manager = collection_manager
        self.study_manager = study_manager
        self.container = ttk.Frame(self, padding=20)
        self.container.pack(fill="both", expand=True)
        self.show_home()

    def show_screen(self, screen, *args):
        for widget in self.container.winfo_children():
            widget.destroy()
        screen(self.container, self, *args).pack(fill="both", expand=True)

    def show_home(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        ttk.Label(self.container, text="My Library", font=("Arial", 22)).pack(pady=15)
        ttk.Button(self.container, text="All Flashcards",
                   command=lambda: self.show_collection(None)).pack(pady=5)
        if self.collection_manager is not None:
            for collection in self.collection_manager.get_all_collections():
                ttk.Button(
                    self.container,
                    text=collection.name,
                    command=lambda cid=collection.id: self.show_collection(cid)
                ).pack(pady=5)
        ttk.Button(self.container, text="+ New Collection",
                   command=self.new_collection).pack(pady=15)

    def new_collection(self):
        if self.collection_manager is None:
            messagebox.showinfo("UI Test", "Backend not connected yet.")
            return

        name = simpledialog.askstring("New Collection", "Collection name:", parent=self)
        if not name:
            return
        try:
            self.collection_manager.create_collection(name)
            self.show_home()
        except ValueError as error:
            messagebox.showerror("Error", str(error))

    def show_collection(self, collection_id=None):
        if self.flashcard_manager is None or self.collection_manager is None:
            messagebox.showinfo("UI Test", "Backend not connected yet.")
            return

        self.show_screen(Collection, collection_id)

    def show_study(self, collection_id=None):
        if self.study_manager is None:
            messagebox.showinfo("UI Test", "Backend not connected yet.")
            return

        self.show_screen(Study, collection_id)


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['tkinter'],  # the names (strs) of imported modules
    #     'allowed-io': [],  # the names (strs) of functions that call print/open/input
    #     'max-line-length': 120
    # })

    # TODO: app.run()
    app = Main()
    app.mainloop()

