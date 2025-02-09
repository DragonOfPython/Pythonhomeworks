""" Write a program that checks if a string starts 
with one word and ends with another.
Example:

Input: "Python is fun!"
Starts with: "Python"
Ends with: "fun!  """

a = str(input("Please, enter the whole sentence: "))
b = str(input("Please, enter the starting word: "))
c = str(input("Please, enter the ending word: "))

x = a.startswith(b)
y = a.endswith(c)

if x and y:
    print(f"The sentence is well structed. it is starting with \"{b}\" and it is ending with \"{c}\".")
elif x:
    print(f"Error occured, please check again. The sentence is starting with \"{b}\", but it is not ending with \"{c}\".")
elif y:
    print(f"Error occured, please check again. The sentence is ending with \"{b}\", but it isn't starting with \"{c}\".")
else:
    print("Error occured. Please check again. It is definetly mistake !!!")