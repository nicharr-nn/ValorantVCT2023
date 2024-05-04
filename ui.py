import tkinter as tk
from tkinter import ttk
import pandas as pd
from graph import Graph

class AppUI(tk.Tk):
    def __init__(self, df=''):
        """Create a new instance of the AppUI class."""
        super().__init__()
        self.title("VALORANT Champions Tour 2023 Player Performance")
        self.__screen_width = self.winfo_screenwidth()
        self.__screen_height = self.winfo_screenheight()
        self.geometry(f"{self.__screen_width}x{self.__screen_height}")
        self.main_frame = ttk.Frame(self)
        self.__df = df
        self.selected_data = []
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
        self.back_btn.place(relx=0.9, rely=0.9, anchor="se")

        self.story_telling_btn = ttk.Button(self, text="Story Telling", command=self.story_page)
        self.story_telling_btn.grid(row=0, column=0, sticky="nw", padx=30, pady=10)

        # select the data to display a graph bar, histogram, boxplot, scatter, and pie
        self.cbb_chart = ttk.Combobox(self, values=["Bar", "Histogram", "Boxplot", "Scatter", "Pie"])
        self.cbb_chart.place(relx=0.7, rely=0.9, anchor="se")

        if key_pressed == "Overall":
            self.cbb_column = ttk.Combobox(self, values=["Number of Agents Played","Rounds Played","Rating","ACS","KD","ADR","KPR","APR","FKPR","FDPR","Kills Max","K","D","A","FK","FD"])
        elif key_pressed == "By Agent":
            self.cbb_column = ttk.Combobox(self, values=["Rounds Played","Rating","ACS","KD","KAST","ADR","KPR","APR","FKPR","FDPR","HSP","CSP","Kills Max","K","D","A","FK","FD"])
        self.cbb_column.place(relx=0.5, rely=0.9, anchor="se")


        self.graph_btn = ttk.Button(self, text="Process", command=self.graph_page)
        self.graph_btn.place(relx=0.8, rely=0.9, anchor="se")

    def graph_page(self):
        self.remove_widgets()


    def story_page(self):
        self.remove_widgets()

    def load_data(self, data):
        if data == "Overall":
            overall_data = pd.read_csv("overall_player_stats.csv")
            self.display_table(overall_data)
        elif data == "By Agent":
            by_agent_data = pd.read_csv("player_stats_by_agent.csv")
            self.display_table(by_agent_data)

    def observer(self, event):
        self.statistic_page(event)

    def remove_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def display_table(self, data):
        self.frame = tk.Frame(self, width=self.__screen_width, height=self.__screen_height // 4)
        self.frame.grid(row=0, column=0, padx=30, pady=20)
        self.frame2 = tk.Frame(self, width=self.__screen_width, height=self.__screen_height // 4, bg="black")
        self.frame2.grid(row=1, column=0, padx=30, pady=20)

        y_scrollbar = tk.Scrollbar(self.frame, orient="vertical")
        y_scrollbar.pack(side="right", fill="y")

        x_scrollbar = tk.Scrollbar(self.frame, orient="horizontal")
        x_scrollbar.pack(side="bottom", fill="x")

        self.tree = ttk.Treeview(self.frame, columns=tuple(data.columns), show="headings")

        for col in data.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        for index, row in data.iterrows():
            self.tree.insert("", "end", values=tuple(row))

        self.tree.pack(side="left", fill="both", expand=True)

        self.tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        y_scrollbar.config(command=self.tree.yview)
        x_scrollbar.config(command=self.tree.xview)

        # second frame

        y_scrollbar2 = tk.Scrollbar(self.frame2, orient="vertical")
        y_scrollbar2.pack(side="right", fill="y")

        x_scrollbar2 = tk.Scrollbar(self.frame2, orient="horizontal")
        x_scrollbar2.pack(side="bottom", fill="x")

        self.tree2 = ttk.Treeview(self.frame2, columns=tuple(data.columns), show="headings")

        for col in data.columns:
            self.tree2.heading(col, text=col)
            self.tree2.column(col, width=100, anchor="center")

        self.tree2.pack(side="left", fill="both", expand=True)

        self.tree2.configure(yscrollcommand=y_scrollbar2.set, xscrollcommand=x_scrollbar2.set)
        y_scrollbar2.config(command=self.tree2.yview)
        x_scrollbar2.config(command=self.tree2.xview)

        self.tree.bind("<ButtonRelease-1>", self.select_item)

    def select_item(self, data):
        str_data = self.tree.item(self.tree.selection())
        self.selected_data.append(str_data['values'])
        self.tree2.insert("", "end", values=str_data['values'])


    def run(self):
        """Display the calculator user interface."""
        self.tk.mainloop()