""" Write a program that takes a list of words and 
joins them into a single string, 
separated by a character (e.g., - or ,).   """

a = str(input("Please, enter a list of words: "))

b = a.split()

c = "-".join(b)

print(c)
