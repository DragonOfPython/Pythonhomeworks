""" Create a program that 
takes a number and checks if it is even or not. """

a = int(input("Please, enter the number: "))
b = int(a%2)
if (b == 0):
    print("Congratulationls, {a} is the even number !!!".format(a=a))
else:
    print("Sorry, {a} is not the even number !!!".format(a=a))
