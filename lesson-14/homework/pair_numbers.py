import numpy as np

# Custom function to calculate the power of a number raised to a given exponent
def custom_power(x, power):
    return x ** power

# Arrays of numbers and powers
numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

# Using numpy.vectorize to apply the custom power function to the pairs of numbers
vectorized_power = np.vectorize(custom_power)
result = vectorized_power(numbers, powers)

print("Numbers:", numbers)
print("Powers:", powers)
print("Result of power calculation:", result)