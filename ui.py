import tkinter as tk
from tkinter import ttk
import pandas as pd

class AppUI(tk.Tk):
    def __init__(self):
        """Create a new instance of the AppUI class."""
        super().__init__()
        self.title("VALORANT Champions Tour 2023 Player Performance")
        self.__screen_width = self.winfo_screenwidth()
        self.__screen_height = self.winfo_screenheight()
        self.geometry(f"{self.__screen_width}x{self.__screen_height}")
        self.main_frame = ttk.Frame(self)
        self.init_components()

    def init_components(self):
        self.display_label = ttk.Label(self, text="VALORANT Champions Tour 2023 Player Performance",
                                       font=("Arial", 16, "bold"))
        self.home_btn = ttk.Button(self, text="Home", command=self.home_page)
        self.exit_btn = ttk.Button(self, text="Exit", command=self.quit)

        self.display_label.place(relx=0.5, rely=0.4, anchor="center")
        self.home_btn.place(relx=0.5, rely=0.5, anchor="center")
        self.exit_btn.place(relx=0.5, rely=0.6, anchor="center")
        # self.home_btn.grid(row=1, column=0, sticky="nsew")
        # self.exit_btn.grid(row=2, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def home_page(self):
        self.remove_widgets()

        self.display_label = ttk.Label(self, text="Choose the players' statistics",
                                       font=("Arial", 16, "bold"))
        self.display_label.place(relx=0.5, rely=0.4, anchor="center")
        self.overall_btn = ttk.Button(self, text="Overall")
        self.overall_btn.bind('<Button>', self.observer)
        self.byagent_btn = ttk.Button(self, text="By Agent")
        self.byagent_btn.bind('<Button>', self.observer)

        self.overall_btn.place(relx=0.4, rely=0.5, anchor="center")
        self.byagent_btn.place(relx=0.6, rely=0.5, anchor="center")

    def statistic_page(self, event):
        key_pressed = event.widget.cget('text')
        self.remove_widgets()
        self.load_data(key_pressed)

        self.back_btn = ttk.Button(self, text="Back", command=self.home_page)
        self.story_telling_btn = ttk.Button(self, text="Story Telling", command=self.story_page)
        self.back_btn.place(relx=0.9, rely=0.9, anchor="se")

    def story_page(self):
        pass

    def load_data(self, data):
        if data == "Overall":
            overall_data = pd.read_csv("overall_player_stats.csv")
        elif data == "By Agent":
            by_agent_data = pd.read_csv("players_stats_by_agent.csv")

    def observer(self, event):
        self.statistic_page(event)

    def remove_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def run(self):
        """Display the calculator user interface."""
        self.tk.mainloop()