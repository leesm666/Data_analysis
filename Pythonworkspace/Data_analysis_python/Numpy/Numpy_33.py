import numpy as np

arr = np.array([[-1.2, -1.3, 0.3],
                [0.9, 0.4, 0],
                [0.5, 0.3, -.1], 
                [0.7, -3.1, 0.8], 
                [0.4, 1.2, 0.5]])

print(arr)
print(np.sin(arr))
print(np.tanh(arr))
print("-------------")

# 각 성분이 NaN인 경우 True를, 안니 경우 False를 반환
print(np.isnan(arr))
print(np.isnan(np.log(arr)))
print("-------------")

# 각 성분이 무한대인 경우 True를, 아닌 경우 False를 반환
print(np.isinf(arr))