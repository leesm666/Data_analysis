import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성
print(sr)
print('-----------')
print(pd.cut(sr, [0,20,40,60]))
print(pd.cut(sr, [0,20,40,60]).value_counts)
print(pd.cut(sr, [0,20,40,60], labels=['C','B','A']))

for i in range(2,4):
    print(i)
    
print(3/3)