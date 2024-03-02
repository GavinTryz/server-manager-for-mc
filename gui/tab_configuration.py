import tkinter as tk
from tkinter import ttk

class TabConfiguration(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = ttk.Label(self, text="Second page")
        label.pack()