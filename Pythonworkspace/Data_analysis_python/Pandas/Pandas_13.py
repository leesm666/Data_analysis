import pandas as pd 

sr = pd.Series(['10', '20', '30', '40', '50'])
sr.index = ['aa', 'bb', 'cc', 'dd', 'ee']
print(sr)
print(sr.str[0])

data = {'aa' : 10, 'bb' : 20, 'cc' : 30, 'dd' : 40, 'ee' : 50}
sr = pd.Series(data)
print(sr)
print(sr.astype(str).str[0])