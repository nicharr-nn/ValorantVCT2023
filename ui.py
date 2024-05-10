import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from PIL import Image, ImageTk
from graph import Graph

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
        self.graph = Graph()
        self.all_players = []
        self.player_selected = None

    def init_components(self):
        background_image = Image.open("vct_bg.png")
        background_image = background_image.resize((self.__screen_width, self.__screen_height))
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(self, image=background_photo)
        background_label.image = background_photo
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.display_label = ttk.Label(self, text="VALORANT Champions Tour 2023 Player Performance",
                                       font=("Arial", 16, "bold"))
        self.home_btn = ttk.Button(self, text="Home", command=self.home_page)
        self.exit_btn = ttk.Button(self, text="Exit", command=self.quit)

        self.display_label.place(relx=0.5, rely=0.4, anchor="center")
        self.home_btn.place(relx=0.5, rely=0.5, anchor="center")
        self.exit_btn.place(relx=0.5, rely=0.6, anchor="center")

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

    def menu_tab(self):
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Menu", menu=self.file_menu)
        self.file_menu.add_command(label="Home", command=self.home_page)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

    def statistic_page(self, event):
        self.key_pressed = event.widget.cget('text')
        self.remove_widgets()
        self.load_data(self.key_pressed)
        self.menu_tab()

        self.back_btn = ttk.Button(self, text="Back", command=self.home_page)
        self.back_btn.place(relx=0.9, rely=0.9, anchor="se")

        self.story_telling_btn = ttk.Button(self, text="Story Telling", command=self.story_page)
        self.story_telling_btn.place(relx=0.1, rely=0.9, anchor="sw")

        if self.key_pressed == "Overall":
            self.cbb_column = ttk.Combobox(self, values=["Number of Agents Played","Rounds Played","Rating",
                                                         "ACS","KD","ADR","KPR","APR","FKPR","FDPR","Kills Max",
                                                         "K","D","A","FK","FD"], state="readonly")

        elif self.key_pressed == "By Agent":
            self.cbb_column = ttk.Combobox(self, values=["Rounds Played", "Rating", "ACS", "KD", "KAST", "ADR",
                                                         "KPR", "APR", "FKPR", "FDPR", "HSP", "CSP", "Kills Max",
                                                         "K", "D", "A", "FK", "FD"], state="readonly")

        self.cbb_chart = ttk.Combobox(self, values=["Bar", "Pie", "Histogram", "Boxplot"], state="readonly")
        self.cbb_chart.place(relx=0.7, rely=0.9, anchor="se")
        self.cbb_column.place(relx=0.5, rely=0.9, anchor="se")

        self.tree.bind("<ButtonRelease-1>", self.select_item)

        self.all_btn = ttk.Button(self, text="All")
        self.all_btn.bind('<Button>', self.select_all)
        self.all_btn.grid(row=1, column=0, sticky="nw", padx=30, pady=10)

        self.clear_btn = ttk.Button(self, text="Clear")
        self.clear_btn.bind('<Button>', self.clear_all)
        self.clear_btn.grid(row=1, column=0, sticky="ne", padx=30, pady=10)

        self.descriptive = ttk.Button(self, text="Descriptive", command=self.descriptive_page)
        self.descriptive.place(relx=0.3, rely=0.9, anchor="se")

        self.graph_btn = ttk.Button(self, text="Process", command=self.graph_page)
        self.graph_btn.place(relx=0.8, rely=0.9, anchor="se")

    def descriptive_page(self):
        self.remove_widgets()
        self.menu_tab()
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
        selected_column = self.cbb_column.get()
        selected_chart = self.cbb_chart.get()
        df = pd.DataFrame(self.selected_data)
        if not self.selected_data:
            messagebox.showinfo("Warning", "Please select a player")
        elif selected_chart == "Bar":
            self.graph.bar_processor(df, selected_column, self.selected_data)
        elif selected_chart == "Pie":
            self.graph.pie_processor(df, selected_column, self.selected_data)
        elif selected_chart == "Histogram":
            self.graph.histogram_processor(df, selected_column, self.selected_data)
        elif selected_chart == "Boxplot":
            self.graph.boxplot_processor(df, selected_column, self.selected_data)
        else:
            messagebox.showinfo("Warning", "Please select a chart and a column")

    def story_page(self):
        self.remove_widgets()
        self.menu_tab()
        self.selected_data = []

        if self.key_pressed == "Overall":
            self.cbb_chart = ttk.Combobox(self, values=["Bar(K,D,A)", "Distribution(Kills Max)",
                                                        "Distribution(Rating)", "Scatter plots(Rating,HSP)",
                                                        "Scatter plots(KD,HSP)"], state="readonly")
        elif self.key_pressed == "By Agent":
            self.cbb_chart = ttk.Combobox(self, values=["Pie(Agent)", "Bar(Rating,HSP)"], state="readonly")
            self.pick_chart_btn = ttk.Button(self, text="Pick", command=self.chart_choose)
            self.pick_chart_btn.grid(row=0, column=1, padx=30, pady=10)

        self.back_btn = ttk.Button(self, text="Back", command=self.home_page)
        self.back_btn.place(relx=0.9, rely=0.9, anchor="se")

        self.cbb_chart.grid(row=0, column=0, sticky="nw", padx=30, pady=10)
        self.graph_btn = ttk.Button(self, text="Process", command=self.graph_page_story)
        self.graph_btn.place(relx=0.8, rely=0.9, anchor="se")

    def chart_choose(self):
        if self.cbb_chart.get() == "Pie(Agent)":
            self.player_selected = ttk.Combobox(self, values=self.get_player_name(), state="readonly")
            self.player_selected.grid(row=1, column=0, sticky="nw", padx=30, pady=10)
        elif self.cbb_chart.get() == "Bar(Rating,HSP)":
            self.player_selected = ttk.Combobox(self, values=self.get_player_name(), state="readonly")
            self.player_selected.grid(row=1, column=0, sticky="nw", padx=30, pady=10)
        else:
            messagebox.showinfo("Done", "Picked!, Please click 'Process' button to view the chart.")

    def graph_page_story(self):
        selected_chart = self.cbb_chart.get()
        if selected_chart == "Bar(K,D,A)":
            df = pd.read_csv("overall_player_stats.csv")
            self.graph.bar_KDA_processor(df)
        elif selected_chart == "Distribution(Kills Max)":
            df = pd.read_csv("overall_player_stats.csv")
            self.graph.histogram_processor(df, "Kills Max", self.selected_data)
        elif selected_chart == "Distribution(Rating)":
            df = pd.read_csv("overall_player_stats.csv")
            self.graph.histogram_processor(df, "Rating", self.selected_data)
        elif selected_chart == "Bar(Rating,HSP)":
            df = pd.DataFrame(self.get_player_info(self.player_selected.get()))
            self.graph.bar_rating_hsp_processor(df)
        elif selected_chart == "Scatter plots(Rating,HSP)":
            df = pd.read_csv("overall_player_stats.csv")
            self.graph.scatter_processor(df, "Rating", "HSP")
        elif selected_chart == "Scatter plots(KD,HSP)":
            df = pd.read_csv("overall_player_stats.csv")
            self.graph.scatter_processor(df, "KD", "HSP")
        elif selected_chart == "Pie(Agent)":
            if not self.player_selected:
                messagebox.showinfo("Warning", "Please click 'Pick' button to select a player.")
            df = pd.DataFrame(self.get_player_info(self.player_selected.get()))
            self.graph.pie_agent_processor(df)
        else:
            messagebox.showinfo("Warning", "Please select a chart.")

    def get_player_info(self, player_name):
        if self.key_pressed == "By Agent":
            player_data = pd.read_csv("player_stats_by_agent.csv")
        elif self.key_pressed == "Overall":
            player_data = pd.read_csv("overall_player_stats.csv")
        player_info = player_data[player_data['Player'] == player_name]
        return player_info

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
        self.frame2.grid(row=2, column=0, padx=30, pady=20)

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

        # second table

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

    def get_player_name(self):
        player_data = pd.read_csv("overall_player_stats.csv")
        for index, row in player_data.iterrows():
            self.all_players.append(row['Player'])
        return self.all_players

    def select_all(self, event):
        for item in self.tree.get_children():
            str_data = self.tree.item(item)
            self.selected_data.append(str_data['values'])
            self.tree2.insert("", "end", values=str_data['values'])

    def clear_all(self, event):
        self.selected_data = []
        for item in self.tree2.get_children():
            self.tree2.delete(item)

    def select_item(self, data):
        str_data = self.tree.item(self.tree.selection())

        if self.key_pressed == "Overall":
            column = ["Player ID","Player","Team","Number of Agents Played","Rounds Played","Rating",
                      "ACS","KD","KAST","ADR","KPR","APR","FKPR","FDPR","HSP","CSP","CL","Kills Max","K","D","A","FK","FD"]
        elif self.key_pressed == "By Agent":
            column = ["Player ID","Player","Team","Agent","Agent Type","Rounds Played","Rating","ACS","KD","KAST","ADR","KPR",
                                                         "APR","FKPR","FDPR","HSP","CSP","Kills Max","K","D",
                                                         "A","FK","FD"]
        dict_data = dict(zip(column, str_data['values']))

        if dict_data not in self.selected_data:
            self.selected_data.append(dict_data)
            self.tree2.insert("", "end", values=str_data['values'])
        else:
            messagebox.showinfo("Warning", "Item already selected")

    def run(self):
        """Display the calculator user interface."""
        self.tk.mainloop()