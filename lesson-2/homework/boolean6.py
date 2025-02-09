""" Create a program that accepts a number and 
checks if it is divisible by both 3 and 5.  """

a = int(input("Please, enter the number: "))
i = a%3
k = a%5

if i == 0 and k ==0:
    print(f"Congratulations !!! The number, a = {a}, you have entered is divisible by both 3 and 5.")
elif i > 0 and k ==0:
    print(f"Nice try !!! The number, a = {a}, you have entered is divisible by 5, but it isn't divisible by 3.")
elif i == 0 and k > 0:
    print(f"Nice try !!! The number, a = {a}, you have entered is divisible by 3, but it isn't divisible by 5.")
else:
    print(f"My bad:) The number, a = {a}, you have entered is not divisible by 3 and 5.")