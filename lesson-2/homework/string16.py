""" Write a program that asks the user for 
a string and a character, then removes all occurrences of 
that character from the string. """

a = str(input("Please, enter a sentence: "))
b = str(input("Please, enter a character: "))

c = b[0]
h = a.count(c)
rch = a.replace(c, '')
print(rch)
