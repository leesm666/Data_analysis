import numpy as np

arr = np.array([22,11,44,33,55])

print(arr.min()) 
print(arr.max()) 

print(arr.argmin()) # 가장 작은 값의 인덱스 변환
print(arr.argmax()) # 가장 큰 값의 인덱스 변환

print(arr.std()) # 표준 편차

# 데이터를 정렬했을때 가운데 값 (= 중앙값)
print(np.median(arr))

# 1사분위수(0.25), 중앙값(0.5), 3사분위수(0.75) 값을 변환
print(np.quantile(arr, [0.25, 0.5, 0.75]))