import numpy as np
import matplotlib.pyplot as plt

# Create x values and compute their logarithm
x = np.linspace(0.1, 10, 400)  # Values from 0.1 to 10 to avoid log(0)
y = np.log(x)

# Plot the log(x) function
plt.plot(x, y, label='log(x)', color='blue')
plt.title('Graph of log(x)')
plt.xlabel('x')
plt.ylabel('log(x)')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()

# Show the plot
plt.show()
