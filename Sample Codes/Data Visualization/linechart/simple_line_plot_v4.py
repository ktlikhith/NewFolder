import matplotlib.pyplot as plt


#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]

x1 = [2,4,6,8]
y1 = [12, 25, 18, 30.8]


#plot data
plt.plot(x, y, linestyle="dotted", marker='^', color="red", label = 'Red Line')	
plt.plot(x1, y1, linestyle="dashdot", marker="*", color="blue", label = 'Blue Example')

#configure  X axes
plt.xlim(0.5,10)
plt.xticks([1,4,7,10])

#configure  Y axes
plt.ylim(10,31.2)
plt.yticks([11, 15, 30, 25])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

# add legend
plt.legend()

#title
plt.title("Simple plot")

#show plot
plt.show()