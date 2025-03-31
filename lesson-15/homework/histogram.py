import matplotlib.pyplot as plt
import numpy as np

# Generate random dataset sampled from a normal distribution
np.random.seed(42)
data = np.random.normal(0, 1, 1000)

# Create a histogram of the data
plt.figure()
plt.hist(data, bins=30, color='skyblue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 1000 Random Values from Normal Distribution')
plt.grid(True)
plt.show()