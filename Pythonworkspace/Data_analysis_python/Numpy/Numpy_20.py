import numpy as np

arr = np.array([44,11,55,22,33])

print(np.sort(arr))
print(np.sort(arr[::-1]))

# arg는 index 변환함수. argsort는 sort한 후 값이 아닌 인덱스 변환 
print(np.argsort(arr))
