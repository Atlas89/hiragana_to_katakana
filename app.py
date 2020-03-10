# -*- coding: utf-8 -*-
from tkinter import *
from guesser.guess import Guess
from constants.constant import *

window = Tk()
window.title(WINDOW_TITLE)
window.geometry(WINDOW_SIZE)

# Guess Label
guess_label = Label(window, text="")
guess_label.place(x=WINDOW_WIDTH/2, y=60, anchor="center")

# Answer Label
answer_label = Label(window, text="")
answer_label.place(x=WINDOW_WIDTH/2, y=120, anchor="center")

# Instantiate the guess class
g = Guess(guess_label=guess_label, answer_label=answer_label)

# Actions button
random_hiragana = Button(window, text="RANDOM HIRAGANA", command=lambda: g.random(HIRAGANA_OPTION))
random_hiragana.grid(column=0, row=0)
random_katakana = Button(window, text="RANDOM KATAKANA", command=lambda: g.random(KATAKANA_OPTION))
random_katakana.grid(column=1, row=0)
random_romanji = Button(window, text="RANDOM ROMANJI", command=lambda: g.random(ROMANJI_OPTION))
random_romanji.grid(column=2, row=0)
answer = Button(window, text="ANSWER", command=g.get_answer)
answer.grid(column=3, row=0)

# Start the app
if __name__ == '__main__':
    # Start the desktop app
    window.mainloop()


