import numpy as np
arr = np.arange(1000).reshape(100, 10)
print(arr)
arr1 = arr.T
print(arr1)
arr2 = np.dot(arr, arr1)
print(arr2)
arr3 = pow(arr, 2)
print(arr3)
sum = arr3.sum()
print(sum)
