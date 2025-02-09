""" 
Ask the user for a sentence and create an acronym 
from the first letters of each word.

Example:
Input: "World Health Organization"
Output: "WHO 

"""
a = str(input("Please enter a sentence: "))
a = a.split()
l = len(a)
c = ""
#b = str(a[0])
#print[b[:1]]
#print(b[:1])
for i in range(l):
      b = a[i]
      c += b[0]

print(c)
      

   
