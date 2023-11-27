import csv
import matplotlib.pylab as plt

f= open('gender.csv', 'r')
data = csv.reader(f)
name = input('찾고 싶은 지역의 이름 입력: ')

result = []

for row in data:
    if name in row[0]:
        for i in range(3,104):
            m = int(row[i].replace(',',''))
            f = int(row[i+103].replace(',','')) 
            result.append(m - f)
        break

plt.bar(range(101), result)
plt.show()