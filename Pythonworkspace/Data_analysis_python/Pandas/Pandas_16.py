import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

print(sr)
print('-------------')
print(sr.idxmax()) # numpy에서는 argmax()이고 pandas 에서는 idxmax()
print(sr[sr <=45].max()) # 점수가 45 이하인 데이터 중 가장 큰 값 
print('-------------') 
print(sr.head(2)) # 앞에서 n개
print(sr.tail(2)) # 뒤에서 n개