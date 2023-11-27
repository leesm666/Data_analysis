import numpy as np

data = np.array([[1,2,3],
                 [7,5,2],
                 [10,1,8],
                 [6,3,4]])

# 다양한 합/평균 axis =0/1 에 따라 행/렬이 바뀜
print(data)
print(data.sum(axis=0)) # 열 별 통계값
print(data.sum(axis=1)) # 행 별 통계값
print(data.sum())
print("-------------")

print(data.mean(axis=0))
print(data.mean(axis=1))
print("-------------")