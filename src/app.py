"""It contains the main window of the application."""

from tkinter import Tk

from src.frames.buttons import ButtonFrame
from src.frames.lessons_table import LessonsTableFrame
from src.frames.program_table import ProgramTableFrame
from src.menus.menu_bar import MenuBar


class App(Tk):
    """It represents the main window of the application."""

    def __init__(self):
        """Initialize the main window of the application."""
        super().__init__()
        self.title("Ana Sayfa")
        self.state("zoomed")
        self.iconbitmap("icon.ico")
        self.columnconfigure(0, weight=1)
        self.__create_widgets()

    def __create_widgets(self):
        """Create all the widgets for the main window."""
        program_table_frame = ProgramTableFrame(self)
        program_table_frame.grid(row=0, column=0)

        lesson_table_frame = LessonsTableFrame(self)
        lesson_table_frame.grid(row=1, column=0)

        button_frame = ButtonFrame(self, lesson_table_frame, program_table_frame)
        button_frame.grid(row=2, column=0)

        menu_bar = MenuBar(self, lesson_table_frame)
        self.config(menu=menu_bar)
