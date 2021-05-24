import numpy as np

arr = np.arange(1000).reshape(100, 10)
print(arr)
arr1 = arr.T  # 转置
print(arr1)
arr2 = np.dot(arr, arr1)  # 内积
print(arr2)
arr3 = pow(arr, 2)  # 平方
print(arr3)
sum = arr3.sum()  # 平方和
print(sum)
