#!/usr/bin/python

from tkinter import *

class MainWindow(Frame):
    """
    The main window to the application.
    Used for opening the quiz and the settings windows.
    """

    @classmethod
    def start(cls, title='Math Quiz'):
        root = Tk()
        root.title(title)
        root.geometry('400x300')
        app = MainWindow(root)
        app.mainloop()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self._config_layout()
        self._config_menubar()

    def _config_layout(self):
        self.pack(fill=BOTH, expand=True)
        self.question = Label(self, text='temp label')
        self.question.place(x=200, y=150)

    def _config_menubar(self):
        self.menubar = Menu(self)

        quiz_cascade = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', menu=quiz_cascade)
        quiz_cascade.add_command(label='Quiz Settings')

        self.master.config(menu=self.menubar)
