import math

def square_task(n):
    for i in range(1, n):
        result = int(math.pow(i,2))
        print(result)
        i += i
    return result

n = 5
result1 = square_task(5)
