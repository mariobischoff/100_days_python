from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randint(-280, 280), random.randint(-250, 250))
        self.velocity = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.velocity)
        if self.xcor() < -300:
            self.goto(random.randint(280, 600), random.randint(-250, 250))


class CarManager:
    def __init__(self):
        self.level = 1
        self.cars = []
        self.start()

    def start(self):
        for i in range(20):
            new_car = Car()
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.move()

    def increase_speed(self):
        for car in self.cars:
            car.velocity += MOVE_INCREMENT
