import pandas as pd 

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

sr.loc['ff'] = 70 # 있으면 수정 없으면 추가
print(sr)

sr.append(pd.Series([80, 90, 100], index=['gg', 'hh', 'ii']))
print(sr)

sr = sr.append(pd.Series([80, 90, 100], index=['gg', 'hh', 'ii']))
print(sr)
