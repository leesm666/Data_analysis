import numpy as np

data1 = [1, 2, 3, 4, 5]
data2 = [1, 2, 3, 3.5, 4]

arr1 = np.array(data1)
print(arr1)
print(arr1.shape) # .shape - > (데이터 수,) 1차원
print("---------------------")

arr2 = np.array([1, 2, 3, 4, 5])
print(arr2)
print(arr2.shape)
print(arr2.dtype)