from turtle import Screen, Turtle
import time
from divide import Divide
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

divide = Divide()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
        ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    ball.move()

screen.exitonclick()