from os import system
from day10.calculator.art import logo

clear = lambda: system('cls')

print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    max_bid = 0
    winner = ""
    for name in bids:
        if max_bid < bids[name]:
            winner = name
            max_bid = bids[name]
    print(f"The winner is {winner.capitalize()} with a bid of {max_bid}")


while not bidding_finished:
    name = input("Whats is your name?: ").lower()
    price = int(input("What's your price?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
