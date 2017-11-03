#!/usr/bin/python

from tkinter import *

class MainWindow(Frame):
    """
    The main window to the application.
    Used for opening the quiz and the settings windows.
    """

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
