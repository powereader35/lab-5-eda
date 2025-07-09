import matplotlib as plt
import pandas as pd

def plot_hist(df, col, bins=20):
    df[col].hist(bins=range(14, 19), align='left', rwidth=0.8, )
    plt.title(f'Histogram of {col}')
    plt.show()


    