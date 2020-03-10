from data.katakana_hiragana import (hiragana, katakana, romanji)
import random

tuples = [(hira, kata, roma) for hira, kata, roma in zip(hiragana, katakana, romanji)]


class Guess:
    def __init__(self, guess_label, answer_label):
        self.guess = None
        self.guess_label = guess_label
        self.answer_label = answer_label

    def random(self, option=0):
        self.reset_label(self.answer_label)
        self.guess = random.choice(tuples)
        self.guess_label.config(text=self.guess[option], fg="black", font="Helvetica 40")

    def get_answer(self):
        if self.guess is None:
            return
        resp = self.guess[0] + ' | ' + self.guess[1] + ' | ' + self.guess[2]
        self.answer_label.config(text=resp, fg="black", font="Helvetica 20")

    @staticmethod
    def reset_label(label):
        label.config(text="")
