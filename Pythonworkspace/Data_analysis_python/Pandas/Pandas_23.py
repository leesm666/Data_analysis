import pandas as pd 
data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}

df = pd.DataFrame(data, index=['a','b','c','d'])
print(df)
print('--------------')
print(df.ndim) # 차원
print(df.shape) # (행, 열)
print(df.shape[0]) # 행의 개수

print(df.size) # 데이터 개수
print(df.T) # transpose