# import colorgram

# def extract_colors(image="day18/hirst-painting/hirst.png", num_of_colors=30):
#     """Return a list of tuple RGB, recive a file location and 
#     number of colors"""
#     colors = colorgram.extract(image, num_of_colors)
#     rgb_colors = []
#     for color in colors:
#         rgb_colors.append(tuple(color.rgb))
#     return rgb_colors


# colors = extract_colors()

# print(colors)

import random
import turtle as t

colors = [(233, 233, 232), (231, 233, 237), (236, 231, 233), 
    (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), 
    (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), 
    (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), 
    (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), 
    (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), 
    (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), 
    (219, 175, 187), (169, 206, 172), (219, 182, 169)]

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
OFFSET_START = (-200, -200)
tim.goto(OFFSET_START)
    

for row in range(10):
    for column in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)
    tim.setposition((OFFSET_START[0], tim.position()[1] + 50))

screen = t.Screen()
screen.exitonclick()
