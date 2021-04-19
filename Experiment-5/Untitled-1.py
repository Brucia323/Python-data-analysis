import matplotlib.pyplot as plt
import numpy as np
from numpy.lib import math
x = np.linspace(0, 2*math.pi)  # 在指定的间隔内返回均匀间隔的数字。
plt.subplot(221)
plt.plot(x, np.sin(x))  # sin
plt.subplot(222)
plt.plot(x, np.cos(x))  # cos
plt.subplot(223)
plt.plot(x, np.log(x))  # log
plt.subplot(224)
plt.plot(x, np.exp(x))  # exp
plt.show()
