from turtle import Turtle, position


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.setup()

    def setup(self):
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(self.position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)