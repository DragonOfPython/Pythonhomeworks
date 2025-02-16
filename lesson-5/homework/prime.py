def is_prime(n):
    if n > 0:
    # prime number start from 2, so we will set the following condition:
        if n < 2:
            return False
    # Now, we can check the given number is the prime or not.
        for i in range(2, n):
            if n % i == 0:         
                result = False
                return result
    
        return True
    else:
        return False
        
print(is_prime(5))
print(is_prime(6))
print(is_prime(-5))