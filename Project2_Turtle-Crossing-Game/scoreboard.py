# import relevant library
from turtle import Turtle

# constants
FONT = ("Courier", 24, "normal")

# create the class "Scoreboard" to update scores after each round win / after losing
class Scoreboard(Turtle):

    def __init__(self):
        """Create the object of class 'Scoreboard(Turtle)'."""
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes out and updates scoreboard accordingly."""
        self.clear()
        self.goto(-280, 255)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(100, 170)

    def point(self):
        """Adds a point and updates the scoreboard after each round win."""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Prints game over when player loses the game and prints out final score."""
        self.goto(0, 0)
        self.write("Game over!\n", align="center", font=FONT)
        self.write(f"Your final score is: {self.score}", align="center", font=FONT)
