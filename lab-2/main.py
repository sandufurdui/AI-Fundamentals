# import numpy as np
# from boid import Boid
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# width = 1000
# height = 1000

# flock = [Boid(*np.random.rand(2)*1000, width, height) for _ in range(50)]

# fig, ax = plt.subplots()

# def update(frame):
#     global flock
#     ax.clear()
#     ax.set_xlim(0, width)
#     ax.set_ylim(0, height)
    
#     for boid in flock:
#         boid.edges()
#         boid.apply_behaviour(flock)
#         boid.update()
#         ax.scatter(boid.position[0], boid.position[1])

# ani = animation.FuncAnimation(fig, update, frames=None, interval=10)
# plt.show()

import numpy as np
from boid import Boid
import matplotlib.pyplot as plt
import matplotlib.animation as animation

width = 1000
height = 1000

flock = [Boid(*np.random.rand(2)*1000, width, height) for _ in range(50)]

fig, ax = plt.subplots()

# Create an empty line object to hold the boid positions
line, = ax.plot([], [], 'o', markersize=3)
def update(frame):
    global flock
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    # Update the positions of all the boids
    positions = np.array([boid.position for boid in flock])

    for boid in flock:
        boid.edges()
        boid.apply_behaviour(flock)
        boid.update()

    # Update the line object with the new positions
    line.set_data(positions[:, 0], positions[:, 1])

    return line,

ani = animation.FuncAnimation(fig, update, frames=None, interval=10, blit=True)
plt.show()
