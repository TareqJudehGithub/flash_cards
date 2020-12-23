from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
from random import choice


# TODO Pick cards randomly:
def is_known_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    # Displaying French keys on the flash card:
    current_card = choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)

    # Flip flash card after 3 seconds:
    flip_timer = window.after(3000, func=flip_card)


# TODO remove the current card, and save it in a new .csv file:
def is_unknown_word():
    global data
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    # index=False disables creating new index to new contents:
    data.to_csv("./data/words_to_learn.csv", index=False)
    is_known_word()


# TODO Flip card from French to English:
def flip_card():
    # Displaying French keys on the flash card:
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


# CONSTANTS:
BACKGROUND_COLOR = "#B1DDC6"
current_card = dict()
data_dict = {}
# Fetching 'French' keys from french.words.csv:
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = pandas.DataFrame(original_data).to_dict(orient="records")
else:
    data_dict = pandas.DataFrame(data).to_dict(orient="records")

# TODO UI Setup
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flip flash card after 3 seconds:
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,
                highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="Title", fill="black",
                                font=("Arial", 25, "italic"))
card_word = canvas.create_text(400, 263, text="Some Text", fill="black",
                               font=("Arial", 30, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

# Buttons:
wrong_image = PhotoImage(file="./images/wrong.png")
x_button = Button(
    image=wrong_image,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    command=is_known_word
)
x_button.grid(column=0, row=1)

correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(
    image=correct_image,
    highlightthickness=0,
    bg=BACKGROUND_COLOR,
    bd=0,
    command=is_unknown_word
)
correct_button.grid(column=1, row=1)

is_known_word()

window.mainloop()
