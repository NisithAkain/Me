import matplotlib.pyplot as plt 
import numpy as np

xpoints = np.array([0,10])
ypoints = np.array([0, 10])

plt.plot(xpoints,ypoints,"o") # or can have plt.bar(xp,yp), plt.pie(xp,yp)
plt.show()