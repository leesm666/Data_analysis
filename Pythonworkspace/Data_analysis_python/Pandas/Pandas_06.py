import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

print(sr + 1)
print(sr * 2)
print(sr[sr > 30])
print(sr[(sr == 30) | (sr == 40)])
print(sr[~((sr >=20) & (sr <= 40))])