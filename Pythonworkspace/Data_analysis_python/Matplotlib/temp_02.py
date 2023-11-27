import csv

#1950 년에 날짜 데이터가 없어서 오류

max_temp = -999 # 최고 기온 값을 저장할 변수
max_date = '' # 최고 기온이 가장 높았던 날짜를 저장할 변수
f = open('seoul.csv', 'r')
data = csv.reader(f)
header = next(data)  # next : 데이터 행 한 줄 스킵

for row in data : 
    if row[-1] == '':
        row[-1] = -999 # -999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1])
    if max_temp < row[-1]:
        max_date = row[0] # 날짜 
        max_temp = row[-1]  # 최고기온
        # 최고 기온 계속 비교후 젤 높은 값이 들어 간다.
        
f.close()
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은 ', max_date + '로' , max_temp, '도 였습니다.')