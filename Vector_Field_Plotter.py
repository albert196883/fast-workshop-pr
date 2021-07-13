import numpy as np
import math as m
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

s = np.linspace(0, 5, 6)
x, y, z = np.meshgrid(s, s, s)

X = m.sqrt(x)
Y = m.sqrt(y)
Z = m.sqrt(z)

ax.quiver(x, y, z, X, Y, Z, length = 1, normalize = True)
ax.set_label("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
plt.show()