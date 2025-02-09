""" Write a Python program to check 
if one string contains another. """

a = str(input("Please, enter main text here:"))
b = str(input("Now, please, enter the string you are going to check: "))
a = a.lower()
b = b.lower()

if b in a:
    print(f"\"{a}\" string contain \"{b}\" string")
else:
    print(f"My apologizes, \"{a}\" string doesn't contain \"{b}\" string. ")