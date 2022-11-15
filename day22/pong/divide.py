from turtle import Turtle


class Divide(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()
        self.draw()

    def setup(self):
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(.2, .5, 1)
        self.goto(0, -250)
        self.setheading(90)

    def draw(self):
        self.forward(30)
        for _ in range(15):
            self.stamp()
            self.forward(30)
