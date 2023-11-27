import csv
import matplotlib.pylab as plt

f= open('gender.csv', 'r')
data = csv.reader(f)
name = input('찾고 싶은 지역의 이름 입력: ')
sumsize = []

for row in data:
    if name in row[0]:
        f = m = 0
        for i in range(0,101):
            m += int(row[i+3].replace(',',''))
            f += int(row[-(i+1)].replace(',',''))
        break

sumsize.append(f)
sumsize.append(m)
print(m, f, sumsize)

plt.rc('font', family = 'Malgun Gothic')
color = ['crimson','darkcyan']
plt.axis('equal')
plt.pie(sumsize, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
plt.title(name + ' 지역의 남녀 성별 비율 ')
plt.show()