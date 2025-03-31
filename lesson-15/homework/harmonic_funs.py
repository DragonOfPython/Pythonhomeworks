import matplotlib.pyplot as plt
import numpy as np

# Generate x values between 0 and 2*pi
x = np.linspace(0, 2*np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot sin(x) and cos(x) on the same graph
plt.figure()
plt.plot(x, y_sin, color='blue', linestyle='-', marker='o', label='sin(x)')
plt.plot(x, y_cos, color='red', linestyle='--', marker='s', label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of sin(x) and cos(x)')
plt.legend()
plt.grid(True)
plt.show()