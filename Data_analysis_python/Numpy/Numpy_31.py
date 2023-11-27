import numpy as np

arr = np.array([[-1.2, -1.3, 0.3],
                [0.9, 0.4, 0],
                [0.5, 0.3, -.1], 
                [0.7, -3.1, 0.8], 
                [0.4, 1.2, 0.5]])

print(arr)
print(np.exp(arr))
print(np.log(arr)) # 상용로그
print(np.log10(arr)) 