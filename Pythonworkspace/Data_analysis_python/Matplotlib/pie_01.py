import matplotlib.pyplot as plt

plt.rc('font', family = 'malgun Gothic')
size = [2441,2312,1031,1233]
label = ['A형','B형','AB형','O형']
color = ['darkmagenta','deeppink','hotpink','pink']
plt.axis('equal') # 동그란 원

plt.pie(size, labels = label, autopct='%.1f%%', explode=(0,0,0.2,0), colors=color)
# explode 돌출여부 
plt.legend()
plt.show()