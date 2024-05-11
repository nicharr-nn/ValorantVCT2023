import numpy as np

class DescriptiveStats:
    def __init__(self, df=None):
        self.df = df

    def mean_val(self, column):
        return np.mean(self.df[column])

    def median_val(self, column):
        return np.median(self.df[column])

    def mode_val(self, column):
        return self.df[column].mode()[0]

    def std_dev(self, column):
        return np.std(self.df[column])

    def var_val(self, column):
        return np.var(self.df[column])

    def min_val(self, column):
        return np.min(self.df[column])

    def max_val(self, column):
        return np.max(self.df[column])

    def range_val(self, column):
        return self.max_val(column) - self.min_val(column)

    def q1_val(self, column):
        return np.percentile(self.df[column], 25)

    def q3_val(self, column):
        return np.percentile(self.df[column], 75)

    def iqr_val(self, column):
        return self.q3_val(column) - self.q1_val(column)
