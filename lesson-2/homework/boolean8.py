""" Create a program that checks 
if a given number is between 10 and 20 (inclusive) """

a = float(input("Please, enter the number: a = "))

if a >= 10 and a <= 20:
    result = True
    print(f"a = {a} is between 10 and 20.")
elif a <=10 and a <=20:
    result = False
    print(f"a = {a} is less than both numbers, 10 and 20.")
elif a <=10 and a >= 20:
    result = False
    print(f"a = {a} is less than 10, but a = {a} is greater than 20.")
else:
    result = False
    print(f"a = {a} isn't between 10 and 20.")