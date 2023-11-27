import pandas as pd


data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

print(sr)
print('------------')
print(pd.cut(sr,5))
print(pd.cut(sr,5,right=False))
print(pd.cut(sr,5).value_counts())