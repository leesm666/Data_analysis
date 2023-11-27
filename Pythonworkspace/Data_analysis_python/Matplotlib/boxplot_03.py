import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r')
data = csv.reader(f)
next(data)

month = []
for i in range(12):
    month.append([])

for row in data:
    if row[-1] != '':
        month[int(row[0].split('-')[1]) -1].append(float(row[-1])) # 0번째 부터여서 -1

plt.boxplot(month)
plt.show()