import matplotlib.pyplot as plt 
import numpy as np 

x= np.array([1,5,6,8,17,16,34,83,1,65,49,53,56,42])
y= np.array([3,67,54,6,17,28,4,54,23,9,11,12,34,57])

plt.xlabel("x")
plt.ylabel("y")
plt.subplot(2,1,1)
plt.plot(x,y)


x= np.array([1,5,6,8,17,16,34,83,1,65,49,53,56,42])
y= np.array([3,67,54,6,17,28,4,54,23,9,11,12,34,57])

plt.xlabel("x")
plt.ylabel("y")
plt.subplot(2,1,2)
plt.plot(x,y)
plt.show()

plt.show()