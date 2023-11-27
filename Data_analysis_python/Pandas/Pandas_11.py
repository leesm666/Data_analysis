import pandas as pd 

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

sr.drop(['aa', 'cc'])
print(sr)

# sr = sr.drop(['aa', 'cc']) # 이렇게 해줘야만 sr이 바뀜 하지만 inplace 적용하면 sr로 안받아도됨

sr.drop(['aa', 'cc'], inplace = True)
print(sr)

sr.drop(sr[sr>=25].index, inplace = True)
print(sr)