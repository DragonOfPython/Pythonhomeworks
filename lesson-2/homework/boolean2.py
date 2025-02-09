""" Create a program that checks if two numbers are equal 
and outputs a message if they are.  """

a = float(input("Please, enter the irst number: a = "))
b = float(input("Please, enter the second number: b = "))

if a == b:
    result = True
    print("Congragulations! a and b numbers are equal to each other.")
else:
    result = False
    print("Sorry, a and b numbers aren't equal to each other.")