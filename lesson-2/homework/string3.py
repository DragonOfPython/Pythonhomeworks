""" 
Write a Python program to:

    1. Take a string input from the user.
    2. Print the length of the string.
    3. Convert the string to uppercase and lowercase.

"""

a = str(input("Please, enter some string input: "))
l = len(a)
b = a.upper()
c = a.lower()

print(f"The length of \"{a}\" is {l}")
print(f"The uppercase version of \"{a}\" is {b}")
print(f"The lowercase version of \"{a}\" is {c}")