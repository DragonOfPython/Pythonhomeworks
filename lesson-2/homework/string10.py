""" Write a program that asks the user for a sentence and 
prints the number of words in it.  """

a = str(input("Please, enter a sentence: "))

l = len(a)
c = " "
s = 1

for i in range(l):
    if a[i] == c:
        s += 1
        continue

print(s)