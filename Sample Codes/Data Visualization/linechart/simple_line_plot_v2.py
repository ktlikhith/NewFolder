import matplotlib.pyplot as plt


#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]


# shows different types of line styles and colors
# https://matplotlib.org/2.0.2/api/lines_api.html

plt.plot(x, y, linestyle="dotted", marker="<", color="red")


plt.show()