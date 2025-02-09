""" Create a program that accepts two strings and 
checks if they have the same length. """

a = str(input("Please, enter the first string: "))
b = str(input("Please, enter the second string: "))

i = len(a)
k = len(b)

if i == k:
    result = True
    print(f"Congratulations, the lengths of a and b strings are same.")
else:
    result = False
    print(f"Unfortunatly, the lengths of a and b strings aren't same. Please, try again")