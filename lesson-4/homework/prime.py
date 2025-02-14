def prime_numbers():
    print("All prime numbers between 1 and 100:")
    for number in range(2, 101):   
        primen = True  
        for i in range(2, number):  
            if number % i == 0:  
                primen = False  # It's not prime
                i += i
                break;  
        if primen:
            print(number)  
        number += number

# Run the function to print prime numbers
prime_numbers()