""" Write a program that counts 
the number of vowels and consonants in a given string. """

a = str(input("Please, enter some word: "))
a = a.lower()
vlist = ['a', 'e', 'i', 'u', 'o']
l = len(a)
vn = 0
for i in range(l):
    if a[i] == vlist[0]:
        vn += i
    elif a[i] == vlist[1]:
        vn += 1
    elif a[i] == vlist[2]:
        vn += 1
    elif a[i] == vlist[3]:
        vn += 1
    elif a[i] == vlist[4]:
        vn += 1
    

cn = l - vn
print(f"The number of vowels and consonants are equal to {vn} and {cn}, respectively.")

