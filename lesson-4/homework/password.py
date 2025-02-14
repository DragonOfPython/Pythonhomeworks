def password_checker():
    password = input("Please enter your own password here: ")
    len1 = len(password)

    if len1 < 8:
        print("Password is too short.")
    for i in password:
        if i == i.isupper():
            print("Password must contain an uppercase letter.")
            break;
    else:
        print("Password is strong.")

password_checker()
