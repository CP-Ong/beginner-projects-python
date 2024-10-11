from tkinter import *
import pandas as pd
from random import choice

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Initialize
current_card = {}
my_dict = {}

# Read files
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    my_dict = original_data.to_dict(orient="records")
else:
    my_dict = data.to_dict(orient="records")

def next_card():
    """Updates the French word."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(my_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background,  image=card_front_img)

    # Set timer off flipping the card (3 seconds)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """Flips the card to show English translation of the French word."""
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def known():
    """Removes known cards."""
    my_dict.remove(current_card)
    updated_data = pd.DataFrame(my_dict)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Create the User Interface (UI)
window = Tk()
window.title("OCP Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set timer off flipping the card (3 seconds)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 140, text="", font=("Arial", 35, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create the buttons cross and check
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=known)
check_button.grid(row=1, column=1)

# Call the next_card() function so it shows what we want for the first run
next_card()

window.mainloop()
