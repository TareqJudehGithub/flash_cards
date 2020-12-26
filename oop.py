from tkinter import Tk, Canvas, PhotoImage, Button
from data_class import Data
import pandas

class FlashCards(Data):
    BG_COLOR = "#B1DDC6"

    def __init__(self):

        # TODO UI Setup
        super().__init__()
        self.window = Tk()
        self.window.title("Flash Cards")
        self.window.config(padx=50, pady=50, bg=self.BG_COLOR)
        # Flip flash card after 3 seconds:
        self.flip_timer = self.window.after(3000, func=self.flip_card)

        self.canvas = Canvas(width=800, height=526, bg=self.BG_COLOR, highlightthickness=0)
        # Card image:
        self.front_image = PhotoImage(file="./images/card_front.png")
        self.back_image = PhotoImage(file="./images/card_back.png")
        self.card_bg = self.canvas.create_image(400, 263, image=self.front_image)
        self.upper_txt = self.canvas.create_text(
            400, 150, text="Title", fill="black", font=("Arial", 25, "italic")
        )
        self.lower_txt = self.canvas.create_text(
            400, 263, text="Word", fill="black",
            font=("Arial", 30, "bold")
        )
        self.canvas.grid(column=0, columnspan=2, row=0)
        # Buttons:
        self.x_image = PhotoImage(file="./images/wrong.png")
        self.check_image = PhotoImage(file="./images/right.png")

        self.x_button = Button(
            image=self.x_image,
            highlightthickness=0,
            bg=self.BG_COLOR,
            bd=0,
            command=self.new_random_word
        )
        self.x_button.grid(column=0, row=1)

        self.check_button = Button(
            image=self.check_image,
            highlightthickness=0,
            bg=self.BG_COLOR,
            bd=0,
            command=self.words_to_learn
        )
        self.check_button.grid(column=1, row=1)

        self.new_random_word()

        self.window.mainloop()

    def new_random_word(self):
        # TODO pick random french word from the .csv file:
        try:
            self.window.after_cancel(self.flip_timer)
            random_word = self.random_word()
        except IndexError:
            self.canvas.itemconfig(self.upper_txt, text="Well done!", fill="black")
            self.canvas.itemconfig(self.lower_txt, text="You've learned all the words.",
                                   fill="black")
        except ValueError:
            pass
        else:
            self.canvas.itemconfig(self.front_image, image=self.front_image)
            self.canvas.itemconfig(self.upper_txt, text="French", fill="black")
            self.canvas.itemconfig(self.lower_txt, text=random_word["French"], fill="black")

    def words_to_learn(self):
        # TODO Save words to learn in a new csv file:

        self.learn_word()
        self.new_random_word()

    def flip_card(self):
        # TODO Flip card from French to English:
        random_word = self.random_word()
        self.canvas.itemconfig(self.upper_txt, text="English", fill="white")
        self.canvas.itemconfig(self.lower_txt, text=random_word["English"], fill="white")
        self.canvas.itemconfig(self.card_bg, image=self.back_image)


# flash_cards = FlashCards()



