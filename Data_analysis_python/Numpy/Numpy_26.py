from cgi import print_directory
from time import process_time_ns
import numpy as np

ax = np.array([[1,2],[3,4]])
ay = np.array([[5,6],[7,8]])

# 1차원으로 풀어서
print(np.append(ax,ay, axis=None))
print("----------------")

# row(행)에 추가
print(np.append(ax, ay, axis =0))
print("----------------")

# column(열)에 추가
print(np.append(ax, ay, axis =1))
print("----------------")
