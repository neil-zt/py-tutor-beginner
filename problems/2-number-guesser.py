"""
Practice Exercise 2: Number Guesser

Create a Python program that simulates a number guessing game using functions:

1. `generate_secret_number()`: 
    Generates a random secret number between 1 and 100.
2. `guess_number(secret_number, guess)`: 
    Compares the player's guess to the secret number and provides feedback (higher, lower, or correct).

Your program should:

1. Generate a secret number using generate_secret_number.
2. Allow the player to input guesses and provide feedback using guess_number.
3. Give the user at most 5 tries.
"""

import random

answer = random.randint(1, 100)

for i in range(7):
    guess = int(input("Guess the number: "))
    if guess > answer:
        print("Your guess is too high!")
    if guess < answer:
        print("Your guess is too low!")
    if guess == answer:
        print("You guessed correctly!")
        break