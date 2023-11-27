import pandas as pd

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('-----------------')
print(df['eng'])
print(df[['eng', 'math']])
print(df['eng']['a':'c'])

print(df[1:3])
print(df['b' : 'c'])