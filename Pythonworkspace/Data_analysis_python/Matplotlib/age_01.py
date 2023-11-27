import csv
import matplotlib.pyplot as plt
import pandas as pd

f = open('age.csv', 'r')
data = csv.reader(f)

result = []
name = ['마천', '거여','성동구']

for row in data:
    for r in range(0, len(name)):
        if name[r] in row[0]:
            # print(row)
            # df = row
            # print(df)
            for i in row[0:]:
                result.append(i)
            
print(result)
df = pd.DataFrame(data=result)
print(df.T)
# df.T
# print(df.T)

# df.to_csv('medi.csv', encoding='utf-8-sig')
# plt.style.use('ggplot')
# plt.title(name + ' 지역의 인구 구조')
# plt.plot(result)
# plt.show()