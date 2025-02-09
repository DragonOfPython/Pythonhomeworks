""" Write a Python program to check if a given string 
is polindrome or not. """

a = str(input("Please, enter some words: "))
if a==a[::-1]:
    print(f"Congragulations, the word, \"{a}\", you have entered is polindrome !!!")
else:
    print(f"Sorry, you have failed. The word, \"{a}\", you have enetered is not polindrome !!!")