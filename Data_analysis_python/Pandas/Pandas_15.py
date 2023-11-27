import pandas as pd

sr = pd.Series(['홍길동', '이순신', '김철수', '김순이', '이홍김'])
sr.index = ['aa', 'bb', 'cc', 'dd', 'ee']

print(sr.str.replace('김', '황', regex=True))
print(sr.str.replace('^김', '황', regex=True))
print(sr.str.replace('김$', '황', regex=True))
print(sr.str.replace('김[철이]', '황', regex=True))
