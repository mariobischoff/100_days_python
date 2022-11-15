import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

moves = [rock, paper, scissors]

player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(moves[player_move])
computer_move = random.randint(0, 2)
print("Computer chose:\n")
print(moves[computer_move])


if player_move >= 3 or player_move < 0:
    print("You typed an invalid number, you lose!")
elif player_move == 0 and computer_move == 2:
    print("You win!")
elif computer_move == 0 and player_move == 2:
    print("You lose!")
elif computer_move > player_move:
    print("You lose!")
elif player_move > computer_move:
    print("You win!")
elif player_move == computer_move:
    print("It's a draw.")
