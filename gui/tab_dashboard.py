import tkinter as tk
from tkinter import ttk

class TabDashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = ttk.Label(self, text="First page")
        label.pack()