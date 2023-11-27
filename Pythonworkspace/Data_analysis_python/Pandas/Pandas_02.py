import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

print(sr)
print(sr.dtype)
print(sr.ndim) # 차원
print(sr.shape)
print(sr.size) # 전체 데이터 개수
print(sr.name)
print(sr.index)
print(sr.values)