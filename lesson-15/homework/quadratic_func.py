import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x) = x^2 - 4x + 4
def f(x):
    return x**2 - 4*x + 4

# Generate x values between -10 and 10
x = np.linspace(-10, 10, 400)
y = f(x)

# Plot the function
plt.figure()
plt.plot(x, y, label=r'$f(x) = x^2 - 4x + 4$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the function $f(x) = x^2 - 4x + 4$')
plt.legend()
plt.grid(True)
plt.show()