""" Make a program 
that converts a given Celsius temperature to Fahrenheit."""

a = float(input("Enter the temperature in Celsius: "))

b = 1.8 * a + 32
print("{a} gradus Celsius is equals to {b} Fahrenheit.".format(a=a, b=b))