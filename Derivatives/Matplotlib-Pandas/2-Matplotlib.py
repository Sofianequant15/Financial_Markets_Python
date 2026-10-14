import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 10)
y = x**2
z = x**3

plt.plot(x, y, label='fonction quadratique')
plt.plot(x, z, c='red', lw=5, label='fonction cubique')
plt.legend()
plt.show()

