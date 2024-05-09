import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self, df=None, title=None, data=None):
        self.df = df
        self.data = data
        self.title = title

    def bar_processor(self, df, title, data):
        window = tk.Toplevel(self.df)
        window.title(title)
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        sns.barplot(x='Player', y=title, data=df, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), horizontalalignment='right')
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def pie_processor(self, df, title, data):
        window = tk.Toplevel(self.df)
        window.title("Pie Chart")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        ax.pie(df[title], labels=df['Player'], autopct='%1.2f%%')
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def histogram_processor(self, df, title, data):
        window = tk.Toplevel(self.df)
        window.title("Histogram")
        fig = plt.figure()
        ax = fig.add_subplot()
        fig.set_size_inches(5, 4)

        sns.histplot(data=df, x=title, ax=ax)
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
