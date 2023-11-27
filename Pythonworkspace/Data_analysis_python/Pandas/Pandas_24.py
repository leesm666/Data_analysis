import pandas as pd 

data = {'eng' : [10, 30, 50, 70],
        'kor' : [20, 40, 60, 80],
        'math' : [90, 50, 20, 70]}

df = pd.DataFrame(data, index=['a', 'b','c','d'])
print(df)
print('-------------------')
print(df.index)
print(df.keys())
print(df.columns)
print('-------------------')
print(df.values)
print(df.dtypes)
print(df.dtypes['eng'])
print('-------------------')
print(df.info())