import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성
sr.loc['cc'] = 40
print(sr)
print('------------')
print(sr.std())
print(sr.median())
print(sr.quantile([0.25,0.5,0.75]))
print('-------------')
print(sr.unique())
print(sr.value_counts())