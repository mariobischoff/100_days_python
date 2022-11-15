import os
from random import choice
from hangman_art import stages, logo
# Read a file that contain words
with open("words.txt", "r", encoding="utf8") as f:
    words = f.readlines()

def clear_console():
    os.system('cls')

# Clear the data (remove "\n" at the end of each line)
words = [word.rstrip("\n") for word in words]
chosen_world = choice(words)

display = ["_" for _ in chosen_world]

end_the_game = False
lives = 6

print(logo)
# print(f"Pssst, the solution is {chosen_world}")

while not end_the_game:
    guess = input("\nGuess a letter: ").lower()
    clear_console()

    if guess in display:
        print(f"You've already guessed {guess}")

    for index, letter in enumerate(chosen_world):
        if letter == guess:
            display[index] = letter


    if guess not in chosen_world:
        print(f"You guessed {guess}, that's not in the word. You loose a life.")
        lives -= 1
        if lives == 0:
            print("You loose.")
            print(f"The solution is {chosen_world}")
            end_the_game = True
            
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_the_game = True
        print("You win.")
    
    
    print(stages[lives])
