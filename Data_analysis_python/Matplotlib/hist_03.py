import csv
import matplotlib.pyplot as plt

f = open('seoul.csv', 'r')
data = csv.reader(f)
next(data) 
aug = [] # 8월 리스트
jan = [] # 1월 리스트

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08' :
            aug.append(float(row[-1]))
        if row[0].split('-')[1] == '01':
            jan.append(float(row[-1]))


plt.hist(aug, bins=100, color='r', label="Aug")
plt.hist(jan, bins=100, color='b', label="Jan")

plt.legend()
plt.show()

