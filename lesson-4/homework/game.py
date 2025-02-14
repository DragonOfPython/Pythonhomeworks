import math
import random

def number_guessing():
    while True:
        selectn = random.randint(1,100)
        i = 0
        urinishlar_soni = 10
        listg = ['Y', 'YES', 'y', 'yes', 'ok']

        #if i < urinishlar_soni:
        for i in range(urinishlar_soni):
            guess = int(input("Please enter your guess: "))

            if guess < selectn:
                print("Too low")
            elif guess > selectn:
                print("Too high")
            else:
                print("You guessed it right!")

        else:
            answer = input("You lost. Want to play again? ")
            answer = answer.lower().strip()
            if answer in listg:
                i = 0
            else:
                print("Thank you for playing. The game ended.") 
                break;

number_guessing()