# Guess The Number Game

import random

secret_number = random.randint(1, 100)

guess = 0

while guess != secret_number:

    guess = int(input("Guess a number between 1 to 100: "))
    
    if guess > secret_number:
        print("Too High. Guess lower.")
    
    elif guess < secret_number:
        print("Too lower. Guess High.")
    
    else:
        print("YAY! You Won you have guessed the right number.")
