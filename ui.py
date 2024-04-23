import tkinter as tk
from tkinter import ttk

class AppUI(tk.Tk):
    def __init__(self):
        """Create a new instance of the AppUI class."""
        super().__init__()
        self.title("VALORANT Champions Tour 2023 Player Performance")
        self.__screen_width = self.winfo_screenwidth()
        self.__screen_height = self.winfo_screenheight()
        self.geometry(f"{self.__screen_width//2}x{self.__screen_height//2}")
        self.load_data()
        self.main_frame = ttk.Frame(self)
        self.init_components()

    def init_components(self):
        self.display_label = ttk.Label(self, text="VALORANT Champions Tour 2023 Player Performance",
                                       font=("Arial", 16, "bold"))
        self.home_btn = ttk.Button(self, text="Home", command=self.home_page)
        self.exit_btn = ttk.Button(self, text="Exit", command=self.quit)

        self.display_label.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.home_btn.grid(row=1, column=0, sticky="nsew")
        self.exit_btn.grid(row=2, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def home_page(self):
        self.display_label.destroy()
        self.home_btn.destroy()
        self.exit_btn.destroy()

        self.display_label = ttk.Label(self, text="Welcome!",
                                       font=("Arial", 16, "bold"))
        self.display_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

    def load_data(self):
        # read_csv
        pass

    def run(self):
        """Display the calculator user interface."""
        self.tk.mainloop()