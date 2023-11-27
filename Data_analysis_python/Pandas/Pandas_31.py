import pandas as pd
import numpy as np

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('----------------')
df['my1'] = [1,2,3,4] # 컬럼이 있으면 수정, 없으면 추가
df['my2'] = df['kor'] + df['eng']
print(df)
print('---------------')
df.loc['e'] = [1, 2, 3, 5, 6] 
print(df)
print('-----------------')
print(df.drop(index=['a', 'c']))
print(df.drop(columns=['eng', 'math']))
print('---------------')
print(df)
df.loc['b':'c', 'kor'] = np.nan
df.loc['c':'d', 'kor'] = np.nan
print(df)
print(df.isna())
print(df.isna().sum())