import csv
import matplotlib.pylab as plt
import math

f= open('gender.csv', 'r')
data = csv.reader(f)
name = input('찾고 싶은 지역의 이름 입력: ')

m= []
f= []
size = []

for row in data:
    if name in row[0]:
        for i in range(3,104):
            male = int(row[i].replace(',',''))
            female = int(row[i+103].replace(',','')) 
            m.append(male)
            f.append(female)
            size.append(math.sqrt(male+female))
        break

plt.style.use('ggplot')
plt.rc('font', family = 'Malgun Gothic')
plt.figure(figsize=(10,5))
plt.title(name + '지역의 성별 인구 그래프')
plt.scatter(m, f, s=size, c=range(101), alpha=0.5, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')
plt.xlabel('남성 인구 수')
plt.ylabel('여성 인구 수')
plt.show()