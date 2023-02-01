#created by Fatih Koyuncu
#fatihkoyuncu99@gmail.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import random
import openpyxl


class MenuBar(Menu):
    def __init__(self, container, ltf):
        super().__init__(container)

        self.ltf = ltf

        menubar = Menu(self, tearoff=0)
        self.add_cascade(label="Dosya", menu=menubar)
        menubar.add_command(label='Aç', command=self.open_file)

    def open_file(self):
        filename = filedialog.askopenfilename(title="Dosya Aç",
                                              filetype=(("xlxs files", ".*xlsx"), ("All Files", "*.")))
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_excel(filename)
            except ValueError and FileNotFoundError:
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

        df_rows = df[
            ['Ders Kodu', 'Ders Adı', 'Öğretim Elemanı', 'Kredi', 'Kontenjan', 'Gün Saat Derslik']].to_numpy().tolist()
        for row in df_rows:
            self.ltf.tree.insert("", "end", values=row)


class ProgramTableFrame(Frame):
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
        hours = ["08.30", "09.30", "10.30", "11.30", "Break", "13.00", "14.00", "15.00", "16.00", "17.00", "18.00",
                 "19.00"]

        for i in range(len(hours) + 1):
            for j in range(len(days) + 1):
                if j == 0 and i == 0:
                    self.b['labelsNo' + str(i) + str(j)] = Label(self, text=" ", borderwidth=1, anchor=CENTER,
                                                                 relief=SOLID, width=30, height=2)
                    self.b['labelsNo' + str(i) + str(j)].grid(row=i, column=j, sticky=EW)
                elif j == 0 and i != 0:
                    self.b['labelsNo' + str(i) + str(j)] = Label(self, text=hours[i - 1], borderwidth=1,
                                                                 anchor=CENTER, relief=SOLID, width=30, height=2)
                    self.b['labelsNo' + str(i) + str(j)].grid(row=i, column=j, sticky=EW)
                elif j != 0 and i == 0:
                    self.b['labelsNo' + str(i) + str(j)] = Label(self, text=days[j - 1], borderwidth=1,
                                                                 anchor=CENTER, relief=SOLID, width=30, height=2)
                    self.b['labelsNo' + str(i) + str(j)].grid(row=i, column=j, sticky=EW)
                elif i == 5:
                    self.b['labelsNo' + str(i) + str(j)] = Label(self, text=hours[i - 1], borderwidth=1,
                                                                 anchor=CENTER, relief=SOLID, width=30, height=2,
                                                                 background="black", foreground="white")
                    self.b['labelsNo' + str(i) + str(j)].grid(row=i, column=j, sticky=EW)
                else:
                    self.b['labelsNo' + str(i) + str(j)] = Label(self, text=" ", borderwidth=1, anchor=CENTER,
                                                                 relief=SOLID, width=30, height=2)
                    self.b['labelsNo' + str(i) + str(j)].grid(row=i, column=j, sticky=EW)

                globals().update(self.b)


class LessonsTableFrame(Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=EW, padx=10, pady=10)
        self.columns = ("Ders Kodu", "Ders Adı", "Öğretim Elemani", "Kredi", "Kontenjan", "Gün Saat Derslik")
        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')

        for col in self.columns:
            self.tree.column(col, anchor=CENTER)
            self.tree.heading(col, text=col)
        self.tree.grid(row=0, column=0, sticky=EW)


class ButtonFrame(Frame):
    def __init__(self, container, ltf, ptf):
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
        selected = self.ltf.tree.focus()
        values = self.ltf.tree.item(selected, 'values')
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
            if self.ptf.b[f'labelsNo{rows[i]}{cols[i]}'].cget("text") == " ":
                count = count + 1

        if count == len(rows):
            for i in range(len(rows)):
                self.ptf.b['labelsNo' + str(rows[i]) + str(cols[i])] = Label(self.ptf, text=values[1],
                                                                             borderwidth=1,
                                                                             anchor=CENTER, relief=SOLID, width=30,
                                                                             height=2,
                                                                             background=color)
                self.ptf.b['labelsNo' + str(rows[i]) + str(cols[i])].grid(row=rows[i], column=cols[i],
                                                                          sticky=EW)
                globals().update(self.ptf.b)
        else:
            messagebox.showerror('Ders Saati Çakışması', 'Ders Saatleri Çakıştığı için Programa Eklenemedi!')

        rows.clear()
        cols.clear()

    def delete(self):
        selected = self.ltf.tree.focus()
        values = self.ltf.tree.item(selected, 'values')
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
            if self.ptf.b[f'labelsNo{rows[i]}{cols[i]}'].cget("text") != " ":
                count = count + 1

        if count == len(rows):
            for i in range(len(rows)):
                self.ptf.b['labelsNo' + str(rows[i]) + str(cols[i])] = Label(self.ptf, text=" ", borderwidth=1,
                                                                             anchor=CENTER, relief=SOLID, width=30,
                                                                             height=2)
                self.ptf.b['labelsNo' + str(rows[i]) + str(cols[i])].grid(row=rows[i], column=cols[i],
                                                                          sticky=EW)
                globals().update(self.ptf.b)
        else:
            messagebox.showerror('Ders Saati Ekli Değil', 'Ders Saatleri Ekli Olmadığından Çıkarılamadı!')

        rows.clear()
        cols.clear()


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Ana Sayfa")
        self.state("zoomed")
        self.iconbitmap("icon.ico")
        self.columnconfigure(0, weight=1)
        self.__create_widgets()

    def __create_widgets(self):
        program_table_frame = ProgramTableFrame(self)
        program_table_frame.grid(row=0, column=0)

        lesson_table_frame = LessonsTableFrame(self)
        lesson_table_frame.grid(row=1, column=0)

        button_frame = ButtonFrame(self, lesson_table_frame, program_table_frame)
        button_frame.grid(row=2, column=0)

        menu_bar = MenuBar(self, lesson_table_frame)
        self.config(menu=menu_bar)


if __name__ == "__main__":
    app = App()
    app.mainloop()

