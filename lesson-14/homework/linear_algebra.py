import numpy as np

# Coefficients matrix
coefficients = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])

# Constants vector
constants = np.array([7, 4, 5])

# Solve the system of equations
solution = np.linalg.solve(coefficients, constants)

print("Solution for x, y, z:")
print(solution)