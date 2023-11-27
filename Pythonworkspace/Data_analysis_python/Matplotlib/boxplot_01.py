import matplotlib.pyplot as plt
import random

# boxplot() : quantile하고 동일 최대, 3/4, 2/4, 1/4, 최솟값 표현 

result = []
for i in range(13):
    result.append(random.randint(1,1000))
print(sorted(result))

plt.boxplot(result)
plt.show()