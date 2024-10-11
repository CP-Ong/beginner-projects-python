# import relevant libraries
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# turtle moves forward when player presses the "Up" key
screen.listen()
screen.onkey(player.move_up, "Up")

# sets the condition to continue or to end the game
game_is_on = True

# starts the game
while game_is_on:
    # time to update the screen
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # detect if the player wins
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.point()
        car_manager.speed_increase()

    # detect if the player loses (touches cars)
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

# ends the game when player clicks on the screen
screen.exitonclick()
