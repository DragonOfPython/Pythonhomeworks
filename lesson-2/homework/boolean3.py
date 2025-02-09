""" Write a program that checks 
if a number is positive and even.  """

a = int(input("Please, enter the number: a = "))
b = a%2

if b==0 and a > 0:
    result = True
    print(f"Congratulations!!! You find it. a = {a} is the positive and even number.")
elif b==0 and a < 0:
    result = False
    print(f"Nice try !!! a = {a} is the even number, but not positive.")
elif b > 0 and a > 0:
    result = False
    print(f"Nice try !!! a = {a} is the positive, but it is not even number.")
else:
    print(f"My bad:). a = {a} is neither positive or even, please try again.")