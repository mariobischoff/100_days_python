# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
#  "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# Your score is **z**."


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_string = (name1 + name2).lower()

count_true = 0
for i in "true":
    count_true += combined_string.count(i)

count_love = 0
for i in "love":
    count_love += combined_string.count(i)

scores = int(str(count_true) + str(count_love))

if scores < 10 or scores > 90:
    print(f"Your score is {scores}, you go together like coke and mentos.")
elif scores >= 40 and scores <= 50:
    print(f"Your score is {scores}, you are alright together.")
else:
    print(f"Your score is {scores}.")