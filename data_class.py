import pandas
from random import choice


class Data:

    def __init__(self):
        self.current_card = dict()
        try:
            self.data = pandas.read_csv("./data/to_learn.csv")
        except FileNotFoundError:
            self.original_data = pandas.read_csv("./data/french_words.csv")
            self.data_dict = pandas.DataFrame(self.original_data).to_dict(
                orient="records")
        else:
            self.data_dict = pandas.DataFrame(self.data).to_dict(
                orient="records")

    def random_word(self):
        # pick random french word from the .csv file:
        self.current_card = choice(self.data_dict)
        return self.current_card

    def learn_word(self):
        # Save words to learn in a new csv file:
        self.data_dict.remove(self.current_card)
        new_data = pandas.DataFrame(self.data_dict)
        new_data.to_csv("./data/words_to_learn.csv", index=False)


