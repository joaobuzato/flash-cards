from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ('Ariel', 40, 'italic')
FONT_WORD = ('Ariel', 60, 'bold')
# ------------- Data ----------------

try:
    data = pd.read_csv(filepath_or_buffer="data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(filepath_or_buffer="data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
next_word = random.choice(to_learn)

# ---------- Buttons ---------------


def flip_card(next_word):

    card.itemconfig(card_image, image=card_back_img)
    card.itemconfig(card_title, text="English", fill='white')
    card.itemconfig(card_word, text=next_word.get('English'), fill='white')


def next_card():
    global next_word
    global flip_timer
    window.after_cancel(flip_timer)
    next_word = random.choice(to_learn)
    card.itemconfig(card_image, image=card_front_img)
    card.itemconfig(card_title, text="French", fill='black')
    card.itemconfig(card_word, text=next_word.get('French'), fill='black')
    flip_timer = window.after(3000, flip_card, next_word)

def end_game():
    pass


def is_known():
    global next_word
    if len(to_learn) <= 0:
        return end_game()
    to_learn.remove(next_word)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv")

    next_card()


window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
card = Canvas(width=800, height=526)
card.config(bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = card.create_image(400, 261, image=card_front_img)
card_title = card.create_text(400, 150, font=FONT_LANGUAGE, text="French") # CHANGE LANGUAGE
card_word = card.create_text(400, 263, font=FONT_WORD, text=next_word.get("French"))  # CHANGE WORD
card.grid(row=0, column=0, columnspan=2)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

flip_timer = window.after(1, next_card)

window.mainloop()
