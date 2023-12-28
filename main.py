# main.py
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Number 1 to {x}? "))
        if guess < random_number:
            print("Sorry. too low.")
        elif guess > random_number:
            print("Sorry. too high.")
    print(f"Correct! Number is {random_number}.")

guess(10)


