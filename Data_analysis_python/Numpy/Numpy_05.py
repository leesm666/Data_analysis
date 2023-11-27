import numpy as np

arr1 = np.arange(10)
print(arr1[0])
print(arr1[4:])
print(arr1[-1])
print("-------------")

arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

print(arr2[2,3])
print(arr2[:,3]) # : --> 행 부분 전체