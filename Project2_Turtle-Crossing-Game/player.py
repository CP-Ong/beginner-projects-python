# import relevant library
from turtle import Turtle

# constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# create the class "Player"
class Player(Turtle):

    def __init__(self):
        """Create the object of class 'Player(Turtle)'."""
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Player (Turtle) moves forwards when user presses the 'Up' key"""
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Player (Turtle) goes back to original position after completing each round"""
        self.goto(STARTING_POSITION)
