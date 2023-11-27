import numpy as np 

arr = np.array([11,22,33,44,55])

print(np.append(arr,[100,200]))
print(np.insert(arr,1,[1,2]))

print(np.delete(arr, [0,2]))