""" Create a program that accepts a number and 
returns the last digit of that number. """

a = int(input("Enter the number: a = "))
b = int(a%10)
print("The last digit of {a} is equals to {b}".format(a=a, b=b))