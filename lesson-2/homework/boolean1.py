""" Write a program that accepts a username and password 
and checks if both are not empty.  """

a = str(input("Please, enter your username: "))
b = str(input("Please, enter your password: "))

if a and b:
    result = True
    print("Congrgulations! Now you are in the system.")
elif a:
    print("Error occured! Please, you have to enter your password also, it is empty, please try again.")
elif b:
    print("Error occured! Please, you have to enter your username also, it is empty, please try again.")
else:
    print("Access denied. You have to enter bot username and password. Please try again.")