import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r')
data = csv.reader(f)
next(data)

day = [[] for i in range(31)] # 파이썬 문법 
print(day)

for row in data:
    if row[-1] !='':
        if row[0].split('-')[1] == '08':
            day[int(row[0].split('-')[2]) -1].append(float(row[-1]))

plt.style.use('ggplot')
plt.figure(figsize=(10,5))
plt.boxplot(day, showfliers=False) # non display of outlier : 동그라미 안나옴
# plt.boxplot(day)
plt.show()