import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

sr['aa'] =100
sr.loc['aa'] = 200
sr.iloc[0] = 300

sr.iloc[1:3] = [1,2]
sr['bb':'cc'] = [3,4]
sr.loc['bb':'cc'] = [5,6]

print(sr)