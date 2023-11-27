import pandas as pd

# DataFrame 시작
d1 = [[1,2],[3,4],[5,6]]
d2 = [(1,2),(3,4),(5,6)]
d3 = [{'kor' : 1, 'eng' : 2},
      {'kor' : 3, 'eng' : 4},
      {'kor' : 5, 'eng' : 6}]
d4 = {'kor' : [1,3,5], 'eng' :[2,4,6]}

df1 = pd.DataFrame(d1, index=['a','b','c'], columns=['eng', 'kor'])
print(df1)
print("----------------")
df2 = pd.DataFrame(d2)
print(df2)
print("---------------")
df3 = pd.DataFrame(d3)
print(df3)
print("---------------")
df4 = pd.DataFrame(d4)
print(df4)
