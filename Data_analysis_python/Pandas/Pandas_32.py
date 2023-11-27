import pandas as pd 
import numpy as np

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('----------------')
df.loc['b':'c','kor'] = np.nan
df.loc['c':'d','math'] = np.nan
print(df)
print(df.fillna(1))
df['kor'] = df['kor'].fillna(3)

print(df)
print('------------------')
print(df.dropna())
print(df.dropna(axis=1))
print(df.dropna(subset=['math']))
