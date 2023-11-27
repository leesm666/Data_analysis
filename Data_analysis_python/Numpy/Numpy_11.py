import numpy as np

arr1 = np.array([[11, 22],
                 [33, 44],
                 [55, 66]])

print(arr1.dtype)
print(arr1.size)
print(arr1.shape)

print(arr1.T) # transpose 전치행렬 : 행 <-> 열 
print(arr1.T.shape)