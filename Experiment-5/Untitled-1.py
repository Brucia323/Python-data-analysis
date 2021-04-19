import matplotlib.pyplot as plt
import numpy as np
from numpy.lib import math
x = np.linspace(0, 2*math.pi)
plt.subplot(221)
plt.plot(x, np.sin(x))
plt.subplot(222)
plt.plot(x, np.cos(x))
plt.subplot(223)
plt.plot(x, np.log(x))
plt.subplot(224)
plt.plot(x, np.exp(x))
plt.show()
