import numpy as np

# Coefficients matrix
coefficients = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])

# Constants vector
constants = np.array([12, -5, 15])

# Solve the system of equations
currents = np.linalg.solve(coefficients, constants)

print("Solution for I1, I2, I3 (currents in the branches):")
print(currents)