import numpy as np


def odd(x):
    return x % 2


arr = np.arange(0, 50, 3)
arr1 = list(filter(odd, arr))
print(arr1)
