import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib.animation import FuncAnimation

x = [1, 2, 3 ,4, 5]
y = [0, 0, 0, 0 ,0]
x2 = [0, 0, 0, 0 ,0]
y2 = [1, 2, 3, 4 ,5]

# plt.style.use("dark_background")

fig, ax = plt.subplots(layout="constrained", figsize=(7.5, 7.2))

grid = np.zeros((10, 10))
grid[:7] = 1
paramDict = dict(marker=".", markersize=20, linestyle="solid", linewidth=4)

ax.plot(x, y, **paramDict)
ax.plot(x2, y2, **paramDict)
ax.grid(True)
# plt.xlim((10, 10))
# plt.ylim((10, 10))

plt.box(False)
plt.imshow(grid, cmap="gray_r")
# plt.show()

limFactor = 1

def update(frame):
    currentX = fig.gca().get_xlim()
    currentY = fig.gca().get_ylim()

    x.append(currentX[0]+1)
    y.append(currentY[0]+1)

    fig.gca().set_xlim((currentX[0]+1, currentX[1]+1))
    fig.gca().set_ylim((currentY[0]+1, currentY[1]+1))

animation = FuncAnimation(fig, update, interval=300)

plt.show()
