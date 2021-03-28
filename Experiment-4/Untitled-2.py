import numpy as np


def odd(x):
    return x % 2


arr = np.arange(0, 50, 3)
arr1 = np.where(odd(arr), -1, arr)
print(arr1)
