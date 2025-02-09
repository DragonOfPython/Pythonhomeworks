""" Ask the user to input a sentence and a word to replace. 
Replace that word with another word provided by the user.
Example:

Input sentence: "I love apples."
Replace: "apples"
With: "oranges"
Output: "I love oranges. """

a = str(input("Please, enter your sentence: "))
b = str(input("If you want to replace some word with another, please type here: "))

l = len(a)
c = " "
s = ""

for i in range(l):
    if a[i] == c:
       #s = a[:i]
       s = a[:i]
       continue

nw = s + " " + b
print(nw)
