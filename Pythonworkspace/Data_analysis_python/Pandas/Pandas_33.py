import pandas as pd

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('----------------')
print(df.sort_values(by='math'))
print(df.sort_values(by='math', ascending=False))
print(df.sort_values(by=['kor','eng'], ascending=False))
print(df.sort_index())
df.loc['c','kor'] = 40
print(df)

