import pandas as pd

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('----------------')

print(df.idxmax())
print(df.idxmax(axis=1))
print(df.median())
print(df.std())
print(df.quantile([0.25,0.5,0.75]))
print(df.count())
print(df.describe())
print(df.describe()['eng'])