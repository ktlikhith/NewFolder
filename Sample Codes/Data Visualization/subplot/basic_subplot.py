import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

x = np.random.randint(20, 100, 20)
y = np.random.randint(20, 100, 20)
ax1.scatter(x,y)
ax1.set_xlabel(' marks')
ax1.set_title('First chart')
ax1.set_yticks([20,40,80])

ax2.plot(x,y)
ax3.set_title('Third chart')
plt.tight_layout()

plt.show()