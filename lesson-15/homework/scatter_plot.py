import matplotlib.pyplot as plt
import numpy as np

# Generate random x and y values
np.random.seed(42)
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

# Create a scatter plot
plt.figure()
plt.scatter(x, y, c='r', marker='o', label='Random Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of 100 Random Points in 2D Space')
plt.legend()
plt.grid(True)
plt.show()