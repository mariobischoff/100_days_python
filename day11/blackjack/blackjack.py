from os import system
from random import choice
from typing import List
from day12.art import logo 

clear = lambda: system("cls")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def change_ace(cards: List[int]):
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

def show_winner(player_card, computer_card):
    print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
    print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
    if len(player_card) == 2 and sum(player_card) == 21 or len(computer_card) == 2 and sum(computer_card) == 21:
        if sum(computer_card) == 21:
            print("You Lose. Opponent has a Blackjack")
        else:
            print("Win with a Blackjack 😎")
    elif sum(player_card) > 21:
        print("You went over. You lose 😭")
    elif abs(sum(player_card) - 21) < abs(sum(computer_card) - 21):
        print("You win 😃")
    elif sum(player_card) == sum(computer_card):
        print("Draw 😆")
    else: 
        print("You went over. You lose 😭")

# Give 2 card for player and computer
player_card = [choice(cards) for i in range(2)]
computer_card = [choice(cards) for i in range(2)]
change_ace(player_card)
change_ace(computer_card)

print(logo)

stand = False

while not stand:
    # show player cards and first computer card
    player_score = sum(player_card)
    print(f"Your cards: {player_card}, current score: {player_score}")
    print(f"Computer's first cards: {computer_card[0]}")

    # check
    if player_score >= 21:
        break

    # stand?
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit == "y":
        player_card.append(choice(cards))
        # 1 instead ace if necessary
        change_ace(player_card)
    else:
        stand = True


computer_score = sum(computer_card)
while player_score != 21 and computer_score < 16:
    computer_card.append(choice(cards))
    # 1 instead ace if necessary
    change_ace(player_card)
    computer_score = sum(computer_card)

show_winner(player_card, computer_card)
