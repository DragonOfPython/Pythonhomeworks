""" Create a program to ask name and year of birth from user 
and tell them their age."""

a = str(input("Could you please tell your name? \n Ok, my name is "))
b = int(input("When was you born? \n Sure, I was born in " ))

c = int(2025 - b)

print("All right, {a}, you are {c} years old, right?".format(a=a, c=c))