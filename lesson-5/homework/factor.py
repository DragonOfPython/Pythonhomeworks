def factor():
    positive_number = int(input("Enter a positive integer: "))
    for i in range(1, positive_number + 1): # iteration 
        if positive_number % i == 0:  # Setting the condition
            print(f"{i} is a factor of {positive_number}")

factor()