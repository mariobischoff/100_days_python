import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move()
    screen.update()

    if player.has_crossed():
        car_manager.increase_speed()
        scoreboard.level_up()
        player.next_level()
    
    for car in car_manager.cars:
        if player.distance(car) < 20 and car.xcor() < 30 and car.xcor() > -30:
            scoreboard.game_over()
            game_is_on = False
    
screen.exitonclick()
