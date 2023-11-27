import numpy as np

arr1 = np.array([11, 22, 33, 44, 55])
print(arr1)

arr2 = arr1[[True, True, False, False, True]]
print(arr2)

print(arr1 > 30)
print(arr1[arr1 > 30])