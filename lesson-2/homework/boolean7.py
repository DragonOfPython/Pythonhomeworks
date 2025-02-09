""" Write a program that checks 
if the sum of two numbers is greater than 50.8. 
Create a program that checks 
if a given number is between 10 and 20 (inclusive). """

a = float(input("Please, enter the first number: "))
b = float(input("Please, enter the second numer: "))
c = a + b
d = 50.8
if c > d:
    result = True
    print(f"The sum of a + b = {a} + {b} = {c} is greater than d = {d}.") 
else:
    result = False
    print(f"The sum of a + b = {a} + {b} = {c} is less than d = {d}.")