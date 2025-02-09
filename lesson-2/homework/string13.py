""" Ask the user for a string and remove all spaces from it. """

a = str(input("Please, enter some text here: "))

b = a.split()
c = "".join(b)
print(c)