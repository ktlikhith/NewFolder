import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x1 = [1, 4, 8, 10]
y1 = np.random.randint(20, 50, 4)

ticks = ['one', 'two', 'three', 'four']
width = 0.8

# bar for first set of values
plt.bar(x1, y1, width = width, color = 'blue', label = 'DSV' )

x2 = [i + width for i in x1]
y2 = np.random.randint(20, 50, 4)
plt.bar(x2, y2, width = width, color = 'orange', label = 'ELE' )

ticksPos = [i+width/2 for i in x1]
plt.xticks(ticksPos, ticks )

plt.legend()
plt.xlabel('Tests')
plt.ylabel('Marks')
plt.title('Internal Marks')
plt.show()