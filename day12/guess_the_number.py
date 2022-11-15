from random import randint
from art import logo
from os import system

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

clear = lambda: system("cls")

def set_difficulty():
    """Ask for player the difficulty and return the number of attempt"""
    difficult = input("Choose a difficult. Type 'easy' or 'hard': ").lower()

    if difficult == "hard":
        attempt = HARD_LEVEL_TURNS
    else:
        attempt = EASY_LEVEL_TURNS
    return attempt

def check(guess, number):
    if guess == number:
        print(f"You got it! The answer was {number}.")
    elif guess > number:
        print("To high.")
    else:
        print("To low.")

clear()

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = randint(1, 100)

    attempt = set_difficulty()

    guess = 0
    while guess != number and attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempt -= 1
        check(guess, number)

    if guess != number:
        print("You've run out of guesses, you lose.")

game()