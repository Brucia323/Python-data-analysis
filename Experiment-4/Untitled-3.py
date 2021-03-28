import numpy as np

arr = list(input().split())
arr = np.rray(arr)
size = arr.size
arr.resize((2, size//2))
print(arr)
