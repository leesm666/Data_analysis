from decimal import DecimalTuple
import pandas as pd
import numpy as np

# 1차원 데이터
myList = [10, 20, 30, 40]
t = (10, 20, 30, 40)
d = {'aa' : 10, 'bb' : 20, 'cc' : 30}

sr1 = pd.Series(myList, index=['Lim', 'Kang', 'Lee', 'Shin'], dtype=np.int32, name='kor')

print(sr1)

sr2 = pd.Series(t)
print(sr2)

sr3 = pd.Series(d, dtype=np.float32)
print(sr3)