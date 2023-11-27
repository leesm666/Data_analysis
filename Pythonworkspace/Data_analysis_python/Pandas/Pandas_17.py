import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

sr.loc['cc'] = 40
print(sr)
print('---------------')
print(sr.nlargest(2)) # top 을 구해주는 함수 -> 역정렬하고 2개만 가지고옴
print(sr.nlargest(2, keep='last')) # 마지막만
print(sr.nlargest(2, keep='all')) # 같은게 있으면 모두 
print(sr.nsmallest(2))
print(sr.sum())
print(sr.mean())