import matplotlib.pyplot as plt
plt.ion()
import seaborn as sns
%matplotlib osx
%config InlineBackend.figure_format = 'retina'
sns.set(
    style='ticks', 
    context='talk', 
    font_scale=0.8, 
    palette="tab20",
    rc={'figure.figsize': (8,6)}
)
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Roboto', 'Fira Sans']
rcParams['font.size'] = 10
rcParams['axes.titlesize'] = 12
rcParams['axes.labelsize'] = 10
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10
%doctest_mode

from rich import print
from rich.pretty import pprint
from rich import pretty
pretty.install()

import numpy as np
import pandas as pd

from importlib import reload
import xai_metrics
from xai_metrics import monotonicity
reload(xai_metrics)



# Example #1: sinusoidal function
def true_func(x):
    return np.sin(8 * np.pi * x) / np.exp(x) + x

n_samples = 100
sigma = 0.1

np.random.seed(42)
x = np.random.rand(n_samples)
y = true_func(x) + sigma * np.random.randn(n_samples)
plt.scatter(x, y)
>>> monotonicity(x, y)
# 0.3391002249399947


# Example #2: the start of a parabola
y = x**2 + sigma * np.random.randn(n_samples)
plt.scatter(x, y)
>>> monotonicity(x, y)
# 0.9285849765592809



# -- Prototyping a model-level monotonicity (xys, w) 
# xys is a list of(x,y) pairs - typically, target-vs-feature
# (sensitivity analysis)