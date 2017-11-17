#!/usr/bin/python

from tkinter import *

from question import Question

class MainWindow(Frame):
    """
    The main window to the application.
    Used for opening the quiz and the settings windows.
    """

    @classmethod
    def start(cls, title='Math Quiz'):
        root = Tk()
        root.title(title)
        root.resizable(False, False)
        app = MainWindow(root)
        app.mainloop()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self._config_layout()
        #self._config_menubar() #TODO: Make all of this work
        self._new_question()

    def submit(self):
        if self.question.answer == int(self.answer_entry.get().strip()):
            self.answer_entry.config(bg='light green')
            self._new_question()
        else:
            self.answer_entry.config(bg='pink')
        self.answer_entry.delete(0, 'end')

    def _new_question(self):
        self.question = Question()
        self.question_text.set(self.question)

    def _config_layout(self):
        pad = 10
        self.grid(padx=pad, pady=pad)
        self.grid_columnconfigure(0, minsize=90)

        Label(self, text='Question:').grid(row=0)
        Label(self, text='Answer:').grid(row=1)

        self.question_text = StringVar()
        self.question_text.set('<filler that is very long bro>')
        Label(self, textvariable=self.question_text).grid(row=0, column=1)

        self.answer_entry = Entry(self)
        self.answer_entry.bind('<Return>', lambda event: self.submit())
        self.answer_entry.grid(row=1, column=1)

    def _config_menubar(self):
        self.menubar = Menu(self)

        quiz_cascade = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', menu=quiz_cascade)
        quiz_cascade.add_command(label='Quiz Settings')

        self.master.config(menu=self.menubar)
