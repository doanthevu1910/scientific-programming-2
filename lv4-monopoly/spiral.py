import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Set up plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Set initial values
radius = 1.0  # radius of the dot
theta = 0.0  # angle of the dot in radians
omega = 0.1  # angular velocity of the dot


# Define a function that updates the plot for each frame
def update(i):
	global radius, theta, omega

	# Decrease radius
	radius *= 0.99

	# Update angle
	theta += omega

	# Set x and y coordinates of the dot
	x = radius * np.cos(theta)
	y = radius * np.sin(theta)

	# Clear the plot and plot the new dot
	ax.clear()
	ax.plot(x, y, 'o')


# Animate the plot
anim = matplotlib.animation.FuncAnimation(fig, update, frames=np.arange(0, 360), interval=20)
plt.show()
