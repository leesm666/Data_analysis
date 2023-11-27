import csv
import matplotlib.pyplot as plt 

f = open('seoul.csv', 'r')
data = csv.reader(f)
next(data)
aug = []

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == '08' :
            aug.append(float(row[-1]))

plt.hist(aug, bins=100, color='r')
plt.show()