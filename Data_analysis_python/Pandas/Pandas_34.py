import pandas as pd

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('----------------')

print(df.min())
print(df.sum())
print(df.sum(axis=1)) # 행
print(df.sum().sum())
print(df.mean())
print(df.mean(axis=1).round(2))