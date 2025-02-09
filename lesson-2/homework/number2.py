""" Write a Python file that asks for 
three numbers and outputs the largest and smallest."""

a = float(input("Enter the first number: a = "))
b = float(input("Enter the second number: b = "))
c = float(input("Enter the third number: c = "))

if (a > b > c):
    print(a, b, c)
    # print("a = {a} > b = {b} > c ={c}".format( a = a, b = b, c = c))
elif (a > c > b):
    print(a, b, c)
elif (b > a > c):
    print(b, a, c)
elif (b > c > a):
    print(b, c, a)
elif (c > b > a):
    print(c, b, a)
else:
    print(c, a, b)
