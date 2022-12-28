import matplotlib.pyplot as plt
from numpy import *

r = linspace(0, 20, 360)
t_range = linspace(0, 2000, 360)

for t in t_range:
	x = r * cos(radians(t))
	y = r * sin(radians(t))
	plt.plot(x, y, 'bo', markersize=10)

	plt.draw()
	plt.pause(0.001)

	plt.clf()

