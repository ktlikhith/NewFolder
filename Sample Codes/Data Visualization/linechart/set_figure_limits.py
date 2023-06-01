import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt



def setup_figure_plot_env(title):
	fig = plt.figure(figsize = (6,6), dpi = 100)
	plt.xlim(0.5, 4.5)
	plt.xticks([1, 2, 3, 4])
	plt.ylim(19.8, 21.2)
	plt.yticks([20, 21, 20.5, 20.8])

	plt.xlabel('This is X')
	plt.ylabel('This is Y')
	plt.title(title)

def get_data():
	x = [1, 2, 3, 4]
	y = [20, 21, 20.5, 20.8]

	return x, y

def show_plot():
	setup_figure_plot_env('Simple Plot')
	x, y = get_data()
	plt.plot(x, y, linestyle = 'dashed', marker ='o', color = 'green')
	plt.show()

if __name__ == '__main__':
	show_plot()