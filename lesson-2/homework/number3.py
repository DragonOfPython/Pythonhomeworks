""" Create a program that 
converts kilometers to meters and centimeters."""

a = float(input("Enter the value you want to convert to meters and centimeters (km): "))
b = a * 1000
c = a * 1e+5
print("{a} km is equals to {b} meters and {c} centimeters, respectively".format(a = a, b = b, c = c))