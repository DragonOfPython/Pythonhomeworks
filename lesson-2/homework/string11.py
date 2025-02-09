""" Write a program to check if a string contains any digits."""

a = str(input("Please, enter a string: "))
#l = len(a)

n = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
l = len(n)

for i in range(l):
    if i < l:
        if a[i] == n[0]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[1]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[2]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[3]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[4]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[5]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[6]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[7]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[8]:
            print("This string contain numbers, please enter another one")
            break
        elif a[i] == n[9]:
            print("This string contain numbers, please enter another one")
            break
        else:
            continue
    else:
        print("Error")