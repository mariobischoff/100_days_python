numbers = [1,2,3]
new_numbers = [number + 1 for number in numbers]
new_numbers


name = "Mario"
new_list = [letter.lower() for letter in name]
new_list


new_list = [n * 2 for n in range(1,5)]
new_list

names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
short_names = [name for name in names if len(name) < 5]
short_names
long_names_caps = [name.upper() for name in names if len(name) > 5]
long_names_caps


# Exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
print(squared_numbers)


# Exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)


# Exercise 3
with open("file1.txt") as file1:
    file1_data = file1.readlines()
    file1_list = [int(number.strip("\n")) for number in file1_data]
    file1_list

with open("file2.txt") as file2:
    file2_data = file2.readlines()
    file2_list = [int(number.strip("\n")) for number in file2_data]
    file2_list

result = [number for number in file1_list if number in file2_list]
result


#Dictionary Comprehension
import random
names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
students_score = {student: random.randint(1,100) for student in names}
students_score

passed_students = {student:score for (student, score) in students_score.items() if score > 60}
passed_students



# Exercice 4
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)


# Exercice 5
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:temp_c*9/5+32 for (day, temp_c) in weather_c.items()}
weather_f


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 57, 88]
}


# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
student_data_frame

# Loop Through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


