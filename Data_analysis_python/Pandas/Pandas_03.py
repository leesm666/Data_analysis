from this import d
import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

print(sr[0])
print(sr[-1])
print(sr['cc'])
print(sr[[0,2]])
print(sr[['cc','dd']])
print(sr[1:3])
print(sr['aa':'cc'])

