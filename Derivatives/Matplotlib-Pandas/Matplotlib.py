import matplotlib.pyplot as plt
import numpy as np

"""
Deux méthodes pour Matplotlib : 
    1. Matplotlib version POO
    2. Matplotlib version basique
"""

x = np.linspace(0, 2, 10)
y = x**2

plt.plot(x, y)
plt.show()

