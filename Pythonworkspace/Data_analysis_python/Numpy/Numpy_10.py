from enum import unique
import numpy as np

v, c = np.unique([1, 2, 2, 3, 3, 3, 4, 4, 5], return_counts=True)
print(v)
print(c)

for a, b in zip(v, c):
    print(a, b)