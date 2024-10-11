# import relevant libraries
from turtle import Turtle
import random

# constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_POSITION = 320

# create the class "CarManager" that generates cars randomly
class CarManager:

    def __init__(self):
        """Create the object of class 'CarManager'."""
        self.all_cars = []
        self.move_speed = 0.1

    def create_car(self):
        """Create cars that moves from right to left."""
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            new_car.goto(X_POSITION, y_position)
            self.all_cars.append(new_car)

    def move(self):
        """Cars moving at given distance per frame."""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_increase(self):
        """Speed of cars increases after each round win."""
        self.move_speed *= 0.9
