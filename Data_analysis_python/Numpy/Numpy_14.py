from unittest import result
import numpy as np

salary = np.array([1000,2000,3000,4000,5000])

result = salary - salary * 0.033
print(result)