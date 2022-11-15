print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
split_people = int(input("How many people to split the bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

result = (total_bill + (total_bill * (percent * 0.01))) / split_people

print(f"Each person should pay: ${result:.1f}")