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