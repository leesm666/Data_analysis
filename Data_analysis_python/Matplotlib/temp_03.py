import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '': # 빈 값이 아니라면
        result.append(float(row[-1])) # 값이 존재할 경우 append(뒤 쪽에 추가 =)

plt.plot(result, 'r') # result 리스트에 저장된 값을 빨간색 그래프로 그리기 
plt.show() # 그래프 나타내기