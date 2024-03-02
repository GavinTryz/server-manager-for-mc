import tkinter as tk
from tkinter import ttk

from gui.tab_dashboard import TabDashboard
from gui.tab_configuration import TabConfiguration

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("This is a title")
        self.geometry("1280x720")

        # Tabs
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(fill='both', expand=True)

        tab_dashboard = TabDashboard(self.tabs)
        self.tabs.add(tab_dashboard, text="Tab 1")

        tab_dashboard = TabConfiguration(self.tabs)
        self.tabs.add(tab_dashboard, text="Tab 2")