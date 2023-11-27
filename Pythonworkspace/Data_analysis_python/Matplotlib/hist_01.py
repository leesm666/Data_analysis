import matplotlib.pylab as plt 
import random

dice = []
for i in range(100) :
    dice.append(random.randint(1,6))
print(dice)


plt.hist(dice, bins=6) # bins : x축의 간격 
plt.show()