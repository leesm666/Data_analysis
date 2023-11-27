import numpy as np 

kor = np.array([60,55,70,30,20,90])

print(np.min(kor)) # kor.min() X 
print(kor[kor >= 80])
print(kor[(kor >=50) & (kor <=80)])
print(kor.mean())
print(kor.sum())