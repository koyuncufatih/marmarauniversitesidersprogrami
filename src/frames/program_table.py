"""Creates a table for the weekly program."""

from tkinter import Frame, Label
from tkinter import EW, SOLID, CENTER


class ProgramTableFrame(Frame):
    """Creates a table for the weekly program."""

    def __init__(self, container):
        super().__init__(container)
        self.grid(row=0, column=0, sticky=EW, padx=10, pady=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        self.b = {}
        days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
        hours = [
            "08.30",
            "09.30",
            "10.30",
            "11.30",
            "Break",
            "13.00",
            "14.00",
            "15.00",
            "16.00",
            "17.00",
            "18.00",
            "19.00",
        ]

        for i in range(len(hours) + 1):
            for j in range(len(days) + 1):
                if j == 0 and i == 0:
                    self.b["labelsNo" + str(i) + str(j)] = Label(
                        self,
                        text=" ",
                        borderwidth=1,
                        anchor=CENTER,
                        relief=SOLID,
                        width=30,
                        height=2,
                    )
                    self.b["labelsNo" + str(i) + str(j)].grid(
                        row=i, column=j, sticky=EW
                    )
                elif j == 0 and i != 0:
                    self.b["labelsNo" + str(i) + str(j)] = Label(
                        self,
                        text=hours[i - 1],
                        borderwidth=1,
                        anchor=CENTER,
                        relief=SOLID,
                        width=30,
                        height=2,
                    )
                    self.b["labelsNo" + str(i) + str(j)].grid(
                        row=i, column=j, sticky=EW
                    )
                elif j != 0 and i == 0:
                    self.b["labelsNo" + str(i) + str(j)] = Label(
                        self,
                        text=days[j - 1],
                        borderwidth=1,
                        anchor=CENTER,
                        relief=SOLID,
                        width=30,
                        height=2,
                    )
                    self.b["labelsNo" + str(i) + str(j)].grid(
                        row=i, column=j, sticky=EW
                    )
                elif i == 5:
                    self.b["labelsNo" + str(i) + str(j)] = Label(
                        self,
                        text=hours[i - 1],
                        borderwidth=1,
                        anchor=CENTER,
                        relief=SOLID,
                        width=30,
                        height=2,
                        background="black",
                        foreground="white",
                    )
                    self.b["labelsNo" + str(i) + str(j)].grid(
                        row=i, column=j, sticky=EW
                    )
                else:
                    self.b["labelsNo" + str(i) + str(j)] = Label(
                        self,
                        text=" ",
                        borderwidth=1,
                        anchor=CENTER,
                        relief=SOLID,
                        width=30,
                        height=2,
                    )
                    self.b["labelsNo" + str(i) + str(j)].grid(
                        row=i, column=j, sticky=EW
                    )

                globals().update(self.b)
