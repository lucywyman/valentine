import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)
x = 3.9*(np.sin(t)**3)
y = (3*np.cos(t))-(1.2*np.cos(2*t))-(0.6*np.cos(3*t))-(0.2*(np.cos(4*t))) -1
plt.plot(x, y, 'r')
plt.axis('equal')
plt.fill_between(x, y, color='red')
plt.show()


