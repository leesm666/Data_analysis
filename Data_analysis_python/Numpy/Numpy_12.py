import numpy as np

arr = np.array([11, 22, 33, 44, 55])
print(arr.dtype)

arr = arr.astype(np.float32) # arr를 float로 변환
print(arr.dtype)

arr2 =  arr.resize(3,2) # 값이 부족
print(arr2)

arr3 = arr.reshape(-1, 2) # -1 : 알아서 결정, 없으면 채움 
print(arr3)