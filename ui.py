import tkinter as tk
from tkinter import ttk

class AppUI(tk.Tk):
    def __init__(self):
        """Create a new instance of the AppUI class."""
        super().__init__()

    def run(self):
        """Display the calculator user interface."""
        self.tk.mainloop()