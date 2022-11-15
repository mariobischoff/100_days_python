from turtle import Turtle, Vec2D

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.setup()
        self.move_speed = 0.1

    def setup(self):
        self.shape('circle')
        self.color('white')
        self.penup()
        # self.goto(.6, .6)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase(self):
        self.x_move += 2
        self.y_move += 2
        print('incrise')