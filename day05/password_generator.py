from random import choice, shuffle
import string

print("Welcome to the PyPassword Generator!")

lenght_password = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

digits = "".join(choice(string.digits) for i in range(num_numbers))
symbols = "".join(choice(string.punctuation) for i in range(num_symbols))
letters = "".join(choice(string.ascii_letters) for i in range(lenght_password - num_numbers - num_symbols))

sequence = list(digits + symbols + letters)
shuffle(sequence)
password = "".join(sequence)

print(f"Here is your password: {password}")
