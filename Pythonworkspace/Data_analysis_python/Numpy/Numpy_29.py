import numpy as np

data = np.array([[1,2,3],
                 [7,5,2],
                 [10,1,8],
                 [6,3,4]])

print(data)
print(np.max(data))
print(data.argmax())
print(data.argmax(axis=0)) # 열에서 가장 큰 값의 index 값 
print(data.argmax(axis=1)) # 행에서 가장 큰 값의 index 값
print("---------------")
