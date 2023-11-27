import numpy as np

arr = np.array([11,130,370,11,44,94,200,30,190])

print(np.where(arr < 100)) # index
print(np.where(arr > 100, 'A', 'B'))

conList = [arr > 200, arr >100, arr >0]
choiceList = ['A', 'B', 'C']
print(np.select(conList,choiceList))