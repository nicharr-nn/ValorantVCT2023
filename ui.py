import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph import Graph
import numpy as np

class AppUI(tk.Tk):
    def __init__(self):
        """Create a new instance of the AppUI class."""
        super().__init__()
        self.title("VALORANT Champions Tour 2023 Player Performance")
        self.__screen_width = self.winfo_screenwidth()
        self.__screen_height = self.winfo_screenheight()
        self.geometry(f"{self.__screen_width}x{self.__screen_height}")
        self.main_frame = ttk.Frame(self)
        self.selected_data = []
        self.init_components()
        # call graph.py
        self.graph = Graph()

    def init_components(self):
        self.display_label = ttk.Label(self, text="VALORANT Champions Tour 2023 Player Performance",
                                       font=("Arial", 16, "bold"))
        self.home_btn = ttk.Button(self, text="Home", command=self.home_page)
        self.exit_btn = ttk.Button(self, text="Exit", command=self.quit)

        self.display_label.place(relx=0.5, rely=0.4, anchor="center")
        self.home_btn.place(relx=0.5, rely=0.5, anchor="center")
        self.exit_btn.place(relx=0.5, rely=0.6, anchor="center")

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
        self.key_pressed = event.widget.cget('text')
        self.remove_widgets()
        self.load_data(self.key_pressed)

        self.back_btn = ttk.Button(self, text="Back", command=self.home_page)
        self.back_btn.place(relx=0.9, rely=0.9, anchor="se")

        self.story_telling_btn = ttk.Button(self, text="Story Telling", command=self.story_page)
        self.story_telling_btn.grid(row=0, column=0, sticky="nw", padx=30, pady=10)

        if self.key_pressed == "Overall":
            # self.cbb_chart = ttk.Combobox(self, values=["Bar(K,D,A)", "(in progress) Distribution(Kills Max)",
            #                                             "(in progress) Scatter plots(Rating,HSP), Scatter plots(KD,HSP)"])
            # self.descriptive = ttk.Combobox(self, values=["Rating, HSP", "KD, HSP"])

            self.cbb_column = ttk.Combobox(self, values=["Number of Agents Played","Rounds Played","Rating",
                                                         "ACS","KD","ADR","KPR","APR","FKPR","FDPR","Kills Max",
                                                         "K","D","A","FK","FD"])
            self.cbb_chart = ttk.Combobox(self, values=["Bar", "Pie", "Line", "Histogram", "Boxplot"])

        elif self.key_pressed == "By Agent":
            self.cbb_chart = ttk.Combobox(self, values=["(in progress) Pie(Agent)", "(in progress)"])

        self.cbb_chart.place(relx=0.7, rely=0.9, anchor="se")
        self.cbb_column.place(relx=0.5, rely=0.9, anchor="se")
        self.descriptive = ttk.Button(self, text="Descriptive", command=self.descriptive_page)
        self.descriptive.place(relx=0.3, rely=0.9, anchor="se")

        self.graph_btn = ttk.Button(self, text="Process", command=self.graph_page)
        self.graph_btn.place(relx=0.8, rely=0.9, anchor="se")

    def descriptive_page(self):
        self.remove_widgets()
        # calculate the descriptive statistics (mean, median, mode, std, min, max) for the selected column
        self.column_selected = ttk.Combobox(self, values=["(in progress) Rating, HSP", "(in progress) KD, HSP"])
        self.column_selected.pack()
        self.process_btn = ttk.Button(self, text="Process", command=self.descrip_calculate)
        self.process_btn.pack()
        self.player_selected = ttk.Combobox(self, values=["Demon1", "in progress"])


    def descrip_calculate(self):
        # calculate the descriptive statistics (mean, median, mode, std, min, max) for the selected column
        df = pd.DataFrame(self.selected_data)

    def graph_page(self):
        # need to be in graph.py
        selected_column = self.cbb_column.get()
        selected_chart = self.cbb_chart.get()
        df = pd.DataFrame(self.selected_data)
        if selected_chart == "Bar":
            self.graph.bar_processor(df, selected_column, self.selected_data)
        elif selected_chart == "Pie":
            self.graph.pie_processor(df, selected_column, self.selected_data)
        elif selected_chart == "Histogram":
            self.graph.histogram_processor(df, selected_column, self.selected_data)
        elif selected_chart == "Boxplot":
            self.graph.boxplot_processor(df, selected_column, self.selected_data)

        # if selected_chart == "Bar(K,D,A)":
        #     window = tk.Toplevel(self)
        #     window.title("Bar Chart (Kills, Death, Assist)")
        #     fig = plt.figure()
        #     ax = fig.add_subplot()
        #     fig.set_size_inches(5, 4)
        #
        #     bar_width = 0.2
        #
        #     x = np.arange(len(df['Player']))
        #
        #     ax.bar(x - bar_width, df['K'], width=bar_width, color='blue', alpha=0.7, label='Kills')
        #     ax.bar(x, df['D'], width=bar_width, color='red', alpha=0.7, label='Deaths')
        #     ax.bar(x + bar_width, df['A'], width=bar_width, color='green', alpha=0.7, label='Assists')
        #
        #     ax.set_xticks(x)
        #     ax.set_xticklabels(df['Player'], rotation=0, fontsize=8)
        #
        #     plt.xlabel("Player", fontsize=8)
        #     plt.ylabel("Kills count", fontsize=8)
        #     plt.legend()
        #
        #     canvas = FigureCanvasTkAgg(fig, master=window)
        #     canvas.draw()
        #     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # elif selected_chart == "Distribution(Kills Max)":
        #     pass

        # elif selected_chart == "Pie(Agent)":
        #     window = tk.Toplevel(self)
        #     window.title("Pie Chart (Agent)")
        #     fig = plt.figure()
        #     ax = fig.add_subplot()
        #     fig.set_size_inches(5, 4)
        #
        #     agent = df['Agent'].value_counts()
        #     ax.pie(agent, labels=agent.index, autopct='%1.1f%%', startangle=90)
        #
        #     canvas = FigureCanvasTkAgg(fig, master=window)
        #     canvas.draw()
        #     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # def show_plot(self, fig):
    #     canvas = FigureCanvasTkAgg(fig, master=self)
    #     canvas.draw()
    #     canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

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
        # self.selected_data.append(str_data['values'])
        if self.key_pressed == "Overall":
            column = ["Player ID","Player","Team","Number of Agents Played","Rounds Played","Rating",
                      "ACS","KD","KAST","ADR","KPR","APR","FKPR","FDPR","HSP","CSP","CL","Kills Max","K","D","A","FK","FD"]
        elif self.key_pressed == "By Agent":
            column = ["Player ID","Player","Team","Agent","Agent Type","Rounds Played","Rating","ACS","KD","KAST","ADR","KPR",
                                                         "APR","FKPR","FDPR","HSP","CSP","Kills Max","K","D",
                                                         "A","FK","FD"]
        dict_data = dict(zip(column, str_data['values']))
        self.selected_data.append(dict_data)
        self.tree2.insert("", "end", values=str_data['values'])


    def run(self):
        """Display the calculator user interface."""
        self.tk.mainloop()