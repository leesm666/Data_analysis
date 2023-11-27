import pandas as pd

sr = pd.Series(['홍길동', '이순신', '김철수', '김순이', '이홍김'])
sr.index = ['aa', 'bb', 'cc', 'dd', 'ee']

print(sr.str.contains('김'))
print(sr[sr.str.contains('^김')]) # 정규식: '김'으로 시작
print(sr[sr.str.contains('김$')]) # '김'으로 끝
print(sr[sr.str.contains('[홍이]')]) # []:문자의 집합 중하나 홍 OR 이
print(sr[sr.str.contains('[홍이]순')]) # 홍순 or 이순
print(sr[sr.str.contains('길동|순이')]) # or 