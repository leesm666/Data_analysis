import pandas as pd

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data, name='국어점수') # 시리즈 생성

print(sr[[True, False, False, True, True]])
print("---------------")
sr.index = [2, 3, 4, 5, 6]
print(sr)
print("---------------")
# print(sr[0]) # error
print(sr[2]) # 부여된 인덱스
print(sr.iloc[0])
print(sr.iloc[0:2])