""" Write a program that takes two numbers and 
prints out the result of integer division and theremainder."""

a = float(input("Enter the first number: a = "))
b = float(input("Enter the second number: b = "))

division = int(a/b)
remainder = int(a%b)

print("The value of integer divison and the remainder of a/b is equals to {m} and {n}".format(m = division, n = remainder))