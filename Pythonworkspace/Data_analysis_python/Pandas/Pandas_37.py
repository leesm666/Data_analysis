import pandas as pd

df = pd.read_csv('hotel.csv', index_col=0)

g = df.groupby('grade')

mydf = g.agg(['sum', 'mean', 'count'])['price']
mydf.columns = ['가격의 총합', '가격의 평균', '가격의 개수']
print(mydf)