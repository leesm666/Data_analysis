import numpy as np

# rand --> 0~1 사이 실수값 반환
print(np.random.rand(5))
print(np.random.rand(2,3))

# randn --> 표준정규분포 (평균0, 편차1)
print(np.random.randn(5)) 
print(np.random.randn(2,3))

print(np.random.choice([1, 2, 3, 4, 5], 1))

print(np.random.choice(np.arange(1,11),5))