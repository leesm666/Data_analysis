import pandas as pd

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('----------------')

print(df[df['eng']> 30])
print(df[(df['kor']==20) | (df['kor']==60)])
print(df[(df['kor']>=20) & (df['kor']<=60)])
print(df[df['kor'].isin([20,40])])