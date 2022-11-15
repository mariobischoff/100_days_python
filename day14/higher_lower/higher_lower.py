from random import choice
from game_data import data
from art import logo, vs
from os import system

clear = lambda: system("cls")

def select_to_compare():
    """Return a selected item from data"""
    selected = choice(data)
    data.remove(selected)
    return selected

def print_items(a, b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

def compare(a, b):
    print_items(a, b)
    a_or_b = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a_or_b == "a" and a["follower_count"] > b["follower_count"]:
        return True
    elif a_or_b == "b" and b["follower_count"] > a["follower_count"]:
        return True
    else:
        return False

def game():
    score = 0
    should_continue = True
    clear()
    print(logo)
    a = select_to_compare()
    while should_continue:
        b = select_to_compare()
        if compare(a, b):
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
            a = b
        else:
            should_continue = False
    print(f"Sorry, that's wrong. Final score {score}")


game()