import pandas as pd 

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}
df = pd.DataFrame(data, index=['a' ,'b', 'c', 'd'])
print(df)
print('----------------')
print(df.query('eng>30')) # df[df['eng']>30]
print(df.query('kor==20 or kor ==60'))
print(df.query('20<=kor<=60'))
# num = 30
# print(df.query(f'eng>{num}')) # 'eng>{}'.format(num)