import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r')
data = csv.reader(f)
next(data)
result = []

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14':
            result.append(float(row[2])) # 2 평균 -1 최고기온
 
 
plt.figure(dpi=100)
plt.plot(result, 'hotpink')
plt.show()