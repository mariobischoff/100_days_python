import random
import turtle as t

tim = t.Turtle()

# #Draw Square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


# #Dashed Line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(distance)
#         tim.right(angle)

# colors = ['coral', 'tomato', 'dark magenta', 'dark magenta', 'dodger blue']

# #Draw different shapes
# distance = 100
# for shapes_side_n in range(3, 10):
#     tim.color(random.choice(colors))
#     draw_shape(shapes_side_n)


# colors = ['medium spring green', 'tomato', 'dark cyan', 'dodger blue']


# #RandonWalk
t.colormode(255)

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

# tim.pen()
tim.speed('fastest')
tim.pensize(15)


for i in range(500):
    tim.color(generate_color())
    tim.setheading(random.choice(directions))
    tim.forward(30)


#Draw Spirograph
# tim.speed('fastest')
# tim.pensize(2)

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(generate_color())
#         tim.circle(150)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(1)







screen = t.Screen()
screen.exitonclick()






