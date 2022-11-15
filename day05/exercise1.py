# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# average_heigh = round(sum(student_heights) / len(student_heights))

sum_height = 0
for height in student_heights:
    sum_height += height
average_heigh = round(sum_height / len(student_heights))

print(average_heigh)

#Write your code below this row 👇