import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

sr.iloc[0] = 100
print(sr)

sr.sort_values(ascending=True, inplace=True)
# sr.sort_values(ascending=False, inplace=True)
print(sr)

sr.sort_index(ascending=0, inplace=True)
print(sr)
