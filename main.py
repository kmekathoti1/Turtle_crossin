import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()



scoreboard=Scoreboard()



screen.listen()
screen.onkey(player.move,"Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_a_car()
    car_manager.move_cars()

    # car_manager.move_cars()
    #detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False


    #check turtle collision with top
    if player.ycor()>280:
        player.reset_player()
        scoreboard.increase_level()
        car_manager.increase_car_speed()






    screen.update()
screen.exitonclick()

