import matplotlib.pyplot as plt
import numpy as np

# Define the functions
def f1(x):
    return x**3

def f2(x):
    return np.sin(x)

def f3(x):
    return np.exp(x)

def f4(x):
    return np.log(x + 1) if x >= 0 else None

# Generate x values
x = np.linspace(-2*np.pi, 2*np.pi, 400)

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot f(x) = x^3
axs[0, 0].plot(x, f1(x), color='blue')
axs[0, 0].set_title('$f(x) = x^3$')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')

# Plot f(x) = sin(x)
axs[0, 1].plot(x, f2(x), color='red')
axs[0, 1].set_title('$f(x) = sin(x)$')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')

# Plot f(x) = e^x
axs[1, 0].plot(x, f3(x), color='green')
axs[1, 0].set_title('$f(x) = e^x$')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')

# Plot f(x) = log(x+1) for x >= 0
x_pos = x[x >= 0]
axs[1, 1].plot(x_pos, f4(x_pos), color='purple')
axs[1, 1].set_title('$f(x) = log(x+1)$ for $x \geq 0$')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')

# Adjust layout
plt.tight_layout()
plt.show()