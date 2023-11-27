import matplotlib.pyplot as plt

plt.title('legend')
plt.plot([10,20,30,40], color='r',label = 'dashed', linestyle = '--') # label 범례 이름
plt.plot([40,30,20,10], 'g',label = 'dotted', ls = ':') # label 범례
plt.legend() # 범례를 최적위치에 나오게
plt.show()