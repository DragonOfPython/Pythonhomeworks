def check(denominator):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        else:
            return denominator(a, b)
    return wrapper
        
@check
def div(a, b):
   c = a / b
   return c

print(div(6,2))
print(div(6,0))