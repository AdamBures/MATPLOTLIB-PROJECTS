import matplotlib.pyplot as plt
import numpy as np

x = [11,6,4,2,1]
#y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [7,8,9,2,4]

label = ["Sleeping", "Being in school", "Doing nothing", "Eating", "Programing"]
color = ["black", "blue", "green", "red", "yellow"]

plt.pie(x, labels=label, colors=color)
#plt.bar(x2, y2, label="Second line", color="orange")
#plt.xlabel("Plot Number")
#plt.ylabel("Interesting")
plt.title("GRAPH")
plt.legend()

plt.show()
