""" Write a program that takes three numbers 
and checks if all of them are different.  """

a = float(input("Please, enter the first number: "))
b = float(input("Please, enter the second number: "))
c = float(input("Please, enter the third number: "))

if a == b and b == c:
    result = False
    print(f"a = {a}, b = {b} and c = {c} are equal numbers, please change them. It is not valid for password.")
elif a == b and b > c or b < c:
    result = False
    print(f"a = {a} and b = {b} are equal, but c = {c} isn't. Please, change others also, the numbers should be different.")
elif a > b or a < b and b == c:
    result = False
    print(f"a = {a} and c = {c} are equal, but b = {b} isn't. Please, change others also, the numbers should be different.")
else:
    result = True
    print(f"Conratulations, a = {a}, b = {b} and c = {c} are different. This is valid for password.")