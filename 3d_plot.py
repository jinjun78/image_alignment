import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import pandas as pd
import numpy as np

df = pd.read_csv('table1.csv')

xvals = []
yvals = []
for x in df['image']:
    floats = [float(m) for m in x.split("_")]
    xvals.append(floats[1])
    yvals.append(100*floats[2])

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.set_xlabel('Max number of matches')
ax.set_ylabel('Proportion good matches (%)')
ax.set_zlabel('Euclidean Distance')
surf = ax.plot_trisurf(xvals, yvals, df['ED2'], linewidth=0.1, antialiased=True)

plt.show()
