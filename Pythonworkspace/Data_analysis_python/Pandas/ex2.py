import pandas as pd

sr = pd.Series([90, 90, 55, 60, 76 ,80, 76, 88, 30, 25], name="국어점수")
sr.index = ['홍길동' ,'이순신', '임꺽정', '정난정', '이이', '이황', '정도전', '임석현1' ,'임석현2', '임석현3']

print(sr)
print("-------------")

# 가장 큰 점수
print(sr.max())

# 큰 점수 이름
# print(sr.idxmax())
print(sr.nlargest(1,keep='all').index)

# # 점수 80점 이상
print(sr[sr>=80])

# # 점수 50 이상 80 이하 
print(sr[(sr>=50) & (sr<=80)])

# # 이름이 임으로 시작하는 데이터
# print(sr.loc[sr.index.str.contains('^임')])
print(sr[sr.index.str.contains('^임')])

# # 점수의 평균 값
print(sr.mean())

# # 점수의 총합 
print(sr.sum())

# # 점수의 표준편차
print(sr.std())

# # 40 이하 데이터 삭제
print(sr.drop(sr[sr<=40].index))

# # 50 이상 가산점 10% 50 미만 20%
print(sr.apply(lambda v: v+(v * 0.1) if v >=50 else v+(v * 0.2)))
print(sr.apply(lambda v: v *1.1 if v >=50 else v*1.2))

# # 점수 top 5
print(sr.nlargest())

# # 점수 범위 설정 후 ,개수
# print(pd.cut(sr, [0,50,70,100]).value_counts())
print(pd.cut(sr, [0,50,70,100]).value_counts().sort_index())
