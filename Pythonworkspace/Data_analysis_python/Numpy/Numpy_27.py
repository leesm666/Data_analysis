import numpy as np

data = np.array([[1,2,3],
                 [7,5,2],
                 [10,1,8],
                 [6,3,4]])

print(data)
print(np.delete(data,[0,2]))
print(np.delete(data,[0,2], axis=0)) # 행 삭제 
print(np.delete(data,[0,2], axis=1)) # 열 삭제
print(np.sort(data, axis=None))
