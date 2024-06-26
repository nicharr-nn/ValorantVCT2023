import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self, df=None, title=None, data=None):
        self.df = df
        self.data = data
        self.title = title

    def bar_processor(self, df, title):
        window = tk.Toplevel(self.df)
        window.title(title)
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        val_str_float = [float(i) for i in df[title]]
        sns.barplot(x='Player', y=val_str_float, data=df, ax=ax)
        plt.title(title, fontsize=6)
        plt.ylabel(title, fontsize=6)
        plt.xlabel("Player", fontsize=6)
        plt.xticks(rotation=90, fontsize=4)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def pie_processor(self, df, title):
        window = tk.Toplevel(self.df)
        window.title("Pie Chart")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        ax.pie(df[title], labels=df['Player'], autopct='%1.2f%%')
        for text in ax.texts:
            text.set_fontsize(6)
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def histogram_processor(self, df, title):
        window = tk.Toplevel(self.df)
        window.title("Histogram")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        if title == 'Kills Max' or title == 'Rating':
            sns.histplot(data=df, x=title, ax=ax, kde=True)
            ax.set_title(title)
        else:
            sns.histplot(data=df, x=title, ax=ax)
            ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def boxplot_processor(self, df, title):
        window = tk.Toplevel(self.df)
        window.title("Boxplot")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        sns.boxplot(data=df, x=title, ax=ax)
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def bar_KDA_processor(self, df):
        window = tk.Toplevel(self.df)
        window.title("Bar Chart (Kills, Death, Assist)")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        bar_width = 0.2

        x = np.arange(len(df['Player']))

        ax.bar(x - bar_width, df['K'], width=bar_width, color='blue', alpha=0.7, label='Kills')
        ax.bar(x, df['D'], width=bar_width, color='red', alpha=0.7, label='Deaths')
        ax.bar(x + bar_width, df['A'], width=bar_width, color='green', alpha=0.7, label='Assists')

        ax.set_xticks(x)
        ax.set_xticklabels(df['Player'], rotation=90, fontsize=3)

        plt.title("Bar graph of KDA for all players", fontsize=6)
        plt.xlabel("Player", fontsize=6)
        plt.ylabel("Frequency", fontsize=6)
        plt.legend(loc='upper right')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def pie_agent_processor(self, df):
        window = tk.Toplevel(self.df)
        window.title("Pie Chart of Agents")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        ax.pie(df['Rounds Played'], labels=df['Agent'], autopct='%1.2f%%')
        ax.set_title("Pie graph of rounds played by each agent")

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def bar_rating_hsp_processor(self, df):
        window = tk.Toplevel(self.df)
        window.title("Bar Chart of Rating and Headshot Percentage")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        bar_width = 0.2

        x = np.arange(len(df['Agent']))

        ax.bar(x - bar_width, df['Rating'], width=bar_width, color='blue', alpha=0.7, label='Rating')
        ax.bar(x, df['HSP'], width=bar_width, color='red', alpha=0.7, label='Headshot %')

        ax.set_xticks(x)
        ax.set_xticklabels(df['Agent'], rotation=90, fontsize=6)

        plt.title("Bar graph of Rating and Headshot Percentage for all agents", fontsize=6)
        plt.xlabel("Agent", fontsize=6)
        plt.ylabel("Frequency", fontsize=6)
        plt.legend(loc='upper right')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def scatter_processor(self, df, first_col, sec_col):
        window = tk.Toplevel(self.df)
        window.title("Scatter Plot")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        sns.scatterplot(data=df, x=first_col, y=sec_col, ax=ax)
        ax.set_title(f"{first_col} vs {sec_col}")

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
