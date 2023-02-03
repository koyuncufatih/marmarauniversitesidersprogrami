"""Creates a menu bar for the main window."""


from tkinter import Menu, filedialog, messagebox
from tkinter import CENTER, W
import pandas as pd


class MenuBar(Menu):
    """Creates a menu bar for the main window."""

    def __init__(self, container, ltf):
        """Creates a menu bar for the main window."""
        super().__init__(container)

        self.ltf = ltf

        menubar = Menu(self, tearoff=0)
        self.add_cascade(label="Dosya", menu=menubar)
        menubar.add_command(label="Aç", command=self.open_file)

    def open_file(self):
        """Opens the file and creates a table."""
        filename = filedialog.askopenfilename(
            title="Dosya Aç", filetype=(("xlxs files", ".*xlsx"), ("All Files", "*."))
        )
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)
            except ValueError:
                messagebox.showerror("Hata", "Dosya Açılamadı")
            except FileNotFoundError:
                messagebox.showerror("Hata", "Dosya Açılamadı")

        self.ltf.tree["column"] = self.ltf.columns
        self.ltf.tree["show"] = "headings"

        for col in self.ltf.tree["column"]:
            if col == "Gün Saat Derslik":
                self.ltf.tree.column(col, anchor=W, width=35)
                self.ltf.tree.heading(col, text=col)
            else:
                self.ltf.tree.column(col, anchor=CENTER, width=35)
                self.ltf.tree.heading(col, text=col)

        df_rows = (
            df[
                [
                    "Ders Kodu",
                    "Ders Adı",
                    "Öğretim Elemanı",
                    "Kredi",
                    "Kontenjan",
                    "Gün Saat Derslik",
                ]
            ]
            .to_numpy()
            .tolist()
        )
        for row in df_rows:
            self.ltf.tree.insert("", "end", values=row)
