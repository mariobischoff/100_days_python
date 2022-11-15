from day11.blackjack.art import logo
from os import system

clear = lambda: system("cls")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculate(num_1: float, num_2: float, op: str) -> float:
    try:
        return operations[op](num_1, num_2)
    except:
        print("Invalid operation")


def calculator():
    print(logo)
    num_1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        op = input("Pick an operation: ")
        num_2 = float(input("What's the next number?: "))
        result = calculate(num_1, num_2, op)
        if result:
            print(f"{num_1} {op} {num_2} = {result:.1f}")

        if input(f"Type 'y' to continue calculation with {result:.1f}, or type 'n' to start a new calculation") == "y":
            num_1 = result
        else:
            should_continue = False
            clear()
            calculator()

calculator()