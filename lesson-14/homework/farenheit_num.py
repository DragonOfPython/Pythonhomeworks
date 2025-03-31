import numpy as np

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Array of temperatures in Fahrenheit
temperatures_fahrenheit = np.array([32, 68, 100, 212, 77])

# Using numpy.vectorize to apply the conversion function to the array of temperatures
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
temperatures_celsius = vectorized_conversion(temperatures_fahrenheit)

print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
print("Temperatures converted to Celsius:", temperatures_celsius)