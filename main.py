from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ('Ariel', 40, 'italic')
FONT_WORD = ('Ariel', 60, 'bold')
# ------------- Data ----------------

df = pd.read_csv(filepath_or_buffer="data/french_words.csv")
to_learn = df.to_dict(orient="records")
word = random.choice(to_learn)

# ---------- Buttons ---------------
def next_card():
    next_word = random.choice(to_learn)
    card.itemconfig(card_title, text="French")
    card.itemconfig(card_word, text=next_word.get('French'))





window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
card = Canvas(width=800, height=526)
card.config(bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card.create_image(400, 261, image=card_front_img)
card_title = card.create_text(400, 150, font=FONT_LANGUAGE, text="French")  # CHANGE LANGUAGE
card_word = card.create_text(400, 263, font=FONT_WORD,text=word.get("French"))  # CHANGE WORD
card.grid(row=0, column=0, columnspan=2)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)




next_card()
window.mainloop()
