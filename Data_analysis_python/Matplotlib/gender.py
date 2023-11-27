import csv
import matplotlib.pylab as plt

f= open('gender.csv', 'r')
data = csv.reader(f)
name = input('찾고 싶은 지역의 이름 입력: ')
m = []
f = []

for row in data:
    if name in row[0]:
        for i in range(0,101):
            m.append(-int(row[i+3].replace(',',''))) # 남성의 데이터 왼쪽으로 (-를 int 앞으로 붙암)
            f.append(int(row[-(i+1)].replace(',',''))) # 여성의 데이터 뒤에서 [-1,-2,-3.....]위치 리버스
            # 천단위에 ,가 찍혀있어서 바꾸기
        break
            
f.reverse()

plt.rc('font', family = 'Malgun Gothic')
plt.figure(figsize=(10,5))
plt.rcParams['axes.unicode_minus'] = False # -부호깨짐방지
plt.title(name + ' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, color = 'b',label='남성')
plt.barh(range(101), f, color = 'r',label='여성')
plt.legend()
plt.show()