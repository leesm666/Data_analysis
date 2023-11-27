import numpy as np 

data = np.array([[1,2,3],
                 [7,5,2],
                 [10,1,8],
                 [6,3,4]])

print(data)
print("-----------")

print(data + 2)
print("-----------")

data[1] += 2 # 1번째 행에 2씩 더함
print(data)

