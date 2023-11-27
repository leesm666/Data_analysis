import pandas as pd

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])

print(df)
print('--------------------')
print(df.iloc[0])
print(df.iloc[0,0])
print(df.iloc[[0,2,3]]) # 0, 2, 3번 행
print(df.iloc[1:, 1])
print(df.iloc[1:,1:])
print(df.iloc[1:3, [0,2]]) # 2, 3번행 과 0,2번 열