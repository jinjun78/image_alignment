import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import pandas as pd
import numpy as np

df = pd.read_csv('table1.csv')
image_name = []
for x in df['image']:
    name = str(x)[2]+str(x)[-4:]
    image_name.append(name)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(0,2,0.1)
Y = df['ED2']
# X, Y = np.meshgrid(X, Y)
Z = df['CC2']

plt.xlabel("image name")
plt.ylabel("Euclidean Distance")
plt.xticks(X, image_name)
# Plot the surface
surf = ax.plot_trisurf(X, Y, Z, linewidth=0.2, antialiased=False)


# # Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# # Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()