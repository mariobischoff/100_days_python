import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)
who_pay_bill = random.randint(0, num_items - 1)

print(f"{names[who_pay_bill]} is going to buy the meal today!")