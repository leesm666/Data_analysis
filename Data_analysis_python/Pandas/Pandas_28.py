import pandas as pd

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('------------')
print(df + 1)
print(df * 2)
print('--------------------')
df['eng'] = [1,2,3,4]
print(df)
print('-------------')
df['eng'] += 2
print(df)
print('--------------')
df.loc['a'] +=2
print(df)
print('-----------------')
df.loc['b':'c', 'kor':] = [[1,2], [3,4]]
print(df)
print('---------------')
df.loc['b':'c', 'kor':] +=2
print(df)