def convert_far_to_cel():
    Fahrenheit = int(input("Enter a temperature in degrees F: "))
    Celsius = (Fahrenheit - 32) * 5/9 # Converting Fahrenheit to Celsius
    Celsius = round(Celsius, 2)

    print(f"{Fahrenheit} degree F = {Celsius} degree C")

convert_far_to_cel()

def convert_cel_to_far():
    Celsius = int(input("Enter a temperature in degrees C: "))
    Fahrenheit = Celsius * 9/5 + 32 # Converting Celsius to Fahrenheit
    Fahrenheit = round(Fahrenheit, 2)

    print(f"{Celsius} degree C = {Fahrenheit} degree F")

convert_cel_to_far()