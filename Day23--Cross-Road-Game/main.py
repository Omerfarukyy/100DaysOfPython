import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(fun=player.move, key="w")
screen.onkey(fun=player.move, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    scoreboard.update_scoreboard()
    if player.ycor() >= 280:
        player.move_home()
        scoreboard.increase_point()
        car_manager.new_level()
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    car_manager.create_cars()
    car_manager.move_cars()

screen.exitonclick()
