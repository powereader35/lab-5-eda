import pytest
import pandas as pd

import sys
import os

from src.plot_utils import plot_hist

import matplotlib as plt
from matplotlib import axes


def test_plot_hist_returns_axes():
    # Create a sample DataFrame
    data = {'age': [1,2,3,4,5,6]}
    df = pd.DataFrame(data)

    ax = plot_hist(df, 'age')
    assert isinstance(ax, plt.axes.Axes)