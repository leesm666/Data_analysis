import numpy as np 

a = np.array([[2,3,2],
              [2,3,2], 
              [4,2,3]])
 
print(np.unique(a, axis= 0)) # 종복 제거
print("--------------------")

b = np.array([[2,3,2],
              [2,3,2],
              [3,2,3]])

print(np.unique(b, axis=1)) # 중복 제거

c = np.array([[2,3,2],
              [2,3,3],
              [3,2,3]])

print(np.unique(c, axis=1)) # 오름차순으로 나옴 2번째 열이 마지막으로 이동