import numpy as np

data = np.array([[1,2,3],
                 [7,5,2],
                 [10,1,8],
                 [6,3,4]])

print(data)
print(data.shape)
print(data[1])
print(data[1,1])
print(data[[0,2,3]]) # 0,2,3 번째 행 
print(data[1:3,1])
print(data[1:,[0,2]])
