import numpy as np
import matplotlib.pyplot as plt

# Define the relationship A = constant / v^2
v = np.linspace(0.1, 10, 100)  # Avoid v = 0 to prevent division by zero
constant = 5
A = constant / v**2

# Plot the graph
plt.figure(figsize=(8,6))
plt.plot(v, A, label=r'$A \propto \frac{1}{v^2}$', color='b')
plt.title('Graph of Surface Area (A) vs Velocity (v)', fontsize=14)
plt.xlabel('Velocity (v)', fontsize=12)
plt.ylabel('Surface Area (A)', fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
