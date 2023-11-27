import numpy as np

name = np.array(['홍길동','김철수','임꺽정','김철이','철이임'])

# '철' 이없으면 -1 반환 & '철'이 있으면 인덱스 반환
print(np.char.find(name,'철'))

# np.char.find(name, '철') ! = -1 이므로 '철'을 포함하는 값의 인덱스 반환 
print(name[np.char.find(name, '철') != -1])