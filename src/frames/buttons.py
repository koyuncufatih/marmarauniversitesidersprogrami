"""Contains the ButtonFrame class."""

import random
from tkinter import Frame, Button, messagebox, Label
from tkinter import CENTER, SOLID, EW


class ButtonFrame(Frame):
    """Handles the events of the buttons and their visual appearance."""

    def __init__(self, container, ltf, ptf):
        """Creates the buttons and their grid layout."""
        super().__init__(container)

        self.ltf = ltf
        self.ptf = ptf

        self.grid(row=2, column=0, sticky=EW)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        add_button = Button(self, text="Ekle", command=self.add)
        delete_button = Button(self, text="Çıkar", command=self.delete)

        add_button.grid(row=0, column=0, sticky=EW, padx=10, pady=10)
        delete_button.grid(row=0, column=1, sticky=EW, padx=10, pady=10)

    def findrow(self, i):
        """Finds the row of the timetable according to the time."""
        if i == "08:30":
            row = 1
        elif i == "09:30":
            row = 2
        elif i == "10:30":
            row = 3
        elif i == "11:30":
            row = 4
        elif i == "13:00":
            row = 6
        elif i == "14:00":
            row = 7
        elif i == "15:00":
            row = 8
        elif i == "16:00":
            row = 9
        elif i == "17:00":
            row = 10
        elif i == "18:00":
            row = 11
        else:
            row = 12
        return row

    def findcol(self, i):
        """Finds the column of the timetable according to the day."""
        if i == "Pazartesi":
            col = 1
        elif i == "Salı":
            col = 2
        elif i == "Çarşamba":
            col = 3
        elif i == "Perşembe":
            col = 4
        else:
            col = 5
        return col

    def add(self):
        """Adds the selected lesson to the timetable."""
        selected = self.ltf.tree.focus()
        values = self.ltf.tree.item(selected, "values")
        count = 0
        color = "%06x" % random.randint(0, 0xFFFFFF)
        color = "#" + color
        lesson_hour = values[5].split()
        lesson_day = []
        lesson_days = []

        for i in lesson_hour:
            lesson_day.append(i)
            count = count + 1
            if count == 5:
                lesson_days.append(lesson_day)
                lesson_day = []
                count = 0

        rows = []
        cols = []

        for i in lesson_days:
            row = self.findrow(i[1])
            col = self.findcol(i[0])
            rows.append(row)
            cols.append(col)

        count = 0

        for i in range(len(rows)):
            if self.ptf.b[f"labelsNo{rows[i]}{cols[i]}"].cget("text") == " ":
                count = count + 1

        if count == len(rows):
            for i in range(len(rows)):
                self.ptf.b["labelsNo" + str(rows[i]) + str(cols[i])] = Label(
                    self.ptf,
                    text=values[1],
                    borderwidth=1,
                    anchor=CENTER,
                    relief=SOLID,
                    width=30,
                    height=2,
                    background=color,
                )
                self.ptf.b["labelsNo" + str(rows[i]) + str(cols[i])].grid(
                    row=rows[i], column=cols[i], sticky=EW
                )
                globals().update(self.ptf.b)
        else:
            messagebox.showerror(
                "Ders Saati Çakışması",
                "Ders Saatleri Çakıştığı için Programa Eklenemedi!",
            )

        rows.clear()
        cols.clear()

    def delete(self):
        """Deletes the selected lesson from the timetable."""
        selected = self.ltf.tree.focus()
        values = self.ltf.tree.item(selected, "values")
        count = 0
        lesson_hour = values[5].split()
        lesson_day = []
        lesson_days = []
        for i in lesson_hour:
            lesson_day.append(i)
            count = count + 1
            if count == 5:
                lesson_days.append(lesson_day)
                lesson_day = []
                count = 0

        rows = []
        cols = []

        for i in lesson_days:
            row = self.findrow(i[1])
            col = self.findcol(i[0])
            rows.append(row)
            cols.append(col)

        count = 0
        for i in range(len(rows)):
            if self.ptf.b[f"labelsNo{rows[i]}{cols[i]}"].cget("text") != " ":
                count = count + 1

        if count == len(rows):
            for i in range(len(rows)):
                self.ptf.b["labelsNo" + str(rows[i]) + str(cols[i])] = Label(
                    self.ptf,
                    text=" ",
                    borderwidth=1,
                    anchor=CENTER,
                    relief=SOLID,
                    width=30,
                    height=2,
                )
                self.ptf.b["labelsNo" + str(rows[i]) + str(cols[i])].grid(
                    row=rows[i], column=cols[i], sticky=EW
                )
                globals().update(self.ptf.b)
        else:
            messagebox.showerror(
                "Ders Saati Ekli Değil", "Ders Saatleri Ekli Olmadığından Çıkarılamadı!"
            )

        rows.clear()
        cols.clear()
