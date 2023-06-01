import matplotlib.pyplot as plt


#define some data
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]


#plot data
plt.plot(x, y, linestyle="dashdot", marker="*", color="blue", label = 'Line Example')	

#configure  X axes
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])

#configure  Y axes
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])

#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")

# add legend
plt.legend()

#title
plt.title("Simple plot")

#show plot
plt.show()