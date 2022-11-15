from art import logo, vs
from game_data import data
from random import choice
from os import system

clear = lambda: system("cls")

def format_data(account):
    """Takes the account data and return the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and return if they got ir right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True

account_b = choice(data)

while game_should_continue:

    account_a = account_b
    account_b = choice(data)

    if account_a == account_b:
        account_b = choice(data)
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
