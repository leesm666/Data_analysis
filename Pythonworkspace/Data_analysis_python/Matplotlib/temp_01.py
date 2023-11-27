import csv

f= open('seoul.csv','r')
data = csv.reader(f, delimiter=',')
cnt = 0

for row in data:
    print(row)
    cnt +=1
    if cnt ==10:
        break

f.close()