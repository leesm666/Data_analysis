import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성
sr.loc['cc'] = 40
print(sr)
print('------------')
print(sr.apply(lambda v: v+1 if v>30 else v+2))
print(sr.apply(lambda v: '합격' if v >=40 else '불합격'))