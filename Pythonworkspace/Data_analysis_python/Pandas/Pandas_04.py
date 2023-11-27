import pandas as pd 

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

print(sr.iloc[0])
print(sr[0])
print(sr.iloc[-1])
print(sr.iloc[2:])
print("--------------")
print(sr.loc['aa']) # loc는 키에 해당되는 것 사용, loc[0] -> error
print(sr.loc['dd':])
print(sr.loc['bb':'dd'])
