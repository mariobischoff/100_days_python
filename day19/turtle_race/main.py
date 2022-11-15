from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", 
    prompt="Which turtle will win the race? Enter a color: "
).lower()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    if len(turtles) >= 1:
        position_y = turtles[-1].position()[1]
        new_turtle.goto(x=-230, y=position_y + 40)
    else:
        new_turtle.goto(x=-230, y=-100)
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()