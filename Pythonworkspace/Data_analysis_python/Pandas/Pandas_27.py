import pandas as pd 

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])

print(df)
print('-----------------')
print(df.loc['a':'c'])
print(df.loc[['a','c','d']])
print(df.loc['b':])
print(df.loc['b':, 'kor':])
print(df.loc['b':'c', ['eng','math']])