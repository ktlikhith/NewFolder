import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = [1, 4, 8, 10]
y = np.random.randint(20, 50, 4)

ticks = ['one', 'two', 'three', 'four']
width = 0.8
plt.bar(x, y, width = width, color = 'blue', label = 'DSV' )
plt.xticks(x, ticks)
plt.legend()
plt.xlabel('Tests')
plt.ylabel('Marks')
plt.title('Internal Marks')
plt.show()