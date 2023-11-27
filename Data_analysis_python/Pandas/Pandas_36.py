import pandas as pd

df = pd.read_csv("hotel.csv", index_col=0) # encoding="cp949" 에러 나면 

print(df.head()) # 위에 다섯개
print('----------------------')
print(df['grade'].unique())
print(df['grade'].value_counts().sort_index())
print('----------------------')


g = df.groupby('grade')
print(g.sum()[['price']])

print(g.mean()[['price']])
print(g.max()[['price']])
print(g.count()[['price']])
# print(g.sum()[['rate']])