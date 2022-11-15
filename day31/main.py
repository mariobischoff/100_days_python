from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}


try:
    data = pd.read_csv("data/words_to_learn.csv", header=None)
except FileNotFoundError:
    original_data = pd.read_csv("data/english_words.csv", header=None)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    current_word_trans = current_card[1]
    canvas.itemconfig(card_title, text="Portugues", fill="white")
    canvas.itemconfig(card_word, text=current_word_trans, fill="white")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_word = current_card[0]
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", encoding="utf-8", index=False, header=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="./img/card_front.png")
card_back_img = PhotoImage(file="./img/card_back.png")

card_background = canvas.create_image(400, 263,image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, font=FONT_LG)
card_word = canvas.create_text(400, 263, font=FONT_WORD)


right = PhotoImage(file="img/right.png")
right_button = Button(image=right, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(column=0, row=1)

wrong = PhotoImage(file="img/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()