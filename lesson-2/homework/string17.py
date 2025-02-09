""" Ask the user for a string and 
replace all the vowels with a symbol (e.g., *). """

a = str(input("Please, enter some text: "))
b = str(input("Please, enter a symbol: "))

lvowels = "aAeEiIuUoO"
for i in lvowels:
    a = a.replace(i,b)

print(a)


