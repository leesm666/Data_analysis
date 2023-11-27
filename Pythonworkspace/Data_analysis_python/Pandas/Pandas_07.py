import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

print(sr[sr.isin([20, 40])])
print("-------------------")
print(sr[sr.isin([60])]) # 없어서 안뜸
print("-------------------")
print(sr[~(sr.isin([20, 40]))])
print(sr[sr.between(20, 40)])
print(sr[sr.index.isin(['aa', 'cc'])])
print(sr[sr.index.isin(['aa', 'gg'])])