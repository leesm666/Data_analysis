import numpy as np

kor = np.array([60,55,70,30,20,90])

print(np.delete(kor, np.where(kor <=40)))

kor[kor>=50] = kor[kor>=50] * 1.1
print(kor)

sorted_kor = np.sort(kor)
print(sorted_kor)
print(sorted_kor[-2:])

for i in range(len(kor)):
    if kor[i] >= 70:
        print(kor[i], '합격')
    else:
        print(kor[i], '불합격')