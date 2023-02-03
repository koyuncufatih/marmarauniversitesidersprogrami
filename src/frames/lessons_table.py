"""Creates the table frame for the lessons."""
from tkinter import Frame, EW, CENTER
from tkinter import ttk


class LessonsTableFrame(Frame):
    """Creates the table frame for the lessons."""

    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=EW, padx=10, pady=10)
        self.columns = (
            "Ders Kodu",
            "Ders Adı",
            "Öğretim Elemani",
            "Kredi",
            "Kontenjan",
            "Gün Saat Derslik",
        )
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.column(col, anchor=CENTER)
            self.tree.heading(col, text=col)
        self.tree.grid(row=0, column=0, sticky=EW)
