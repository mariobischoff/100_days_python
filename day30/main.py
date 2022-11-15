# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileExistsError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")


# height = float(input("height: "))
# weight = float(input("weight: "))

# if height > 3:
#     raise ValueError("Human Heigh should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)



# fruits = ['apple', 'pear', 'orange']

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         fruit = 'Fruit'
#     finally:
#         print(fruit + ' pie')

# make_pie(4)

facebook_posts = [
    {'likes': 21, 'comments': 2},
    {'likes': 21, 'comments': 2, 'shares': 1},
    {'likes': 21, 'comments': 2, 'shares': 3},
    {'comments': 21, 'shares': 2},
    {'comments': 21, 'shares': 2},
    {'likes': 21, 'comments': 2},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['likes']
    except KeyError:
        pass
    
print(total_likes)