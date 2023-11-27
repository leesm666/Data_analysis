import matplotlib.pyplot as plt
import random

x = []
y = []
size = []

for i in range(100):
    x.append(random.randint(50,100))
    y.append(random.randint(50,100))
    size.append(random.randint(10,100))

plt.style.use('ggplot')

plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()