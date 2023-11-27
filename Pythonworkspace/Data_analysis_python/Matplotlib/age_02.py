import csv
import matplotlib.pyplot as plt

# 막대 그래프로 그리기
f = open('age.csv', 'r')
data = csv.reader(f)

result = []
name = input('인구 구조가 알고 싶은 지역 이름 입력: ')

for row in data:
    if name in row[0]:
        print(row[0])
        for i in row[3:]:
            result.append(int(i))

plt.bar(range(101), result)
plt.show()