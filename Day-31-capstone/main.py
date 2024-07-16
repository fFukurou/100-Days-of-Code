#Flash Card Project
from tkinter import * #type: ignore
from tkinter import messagebox
import random
import pandas as pd
import math

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- SHOWING FLASH CARDS ------------------------------- #

try:
    dataframe = pd.read_csv("Day-31-capstone/data/words_to_learn.csv")

except FileNotFoundError:
    original_dataframe = pd.read_csv("Day-31-capstone/data/french_words.csv")

    to_learn = original_dataframe.to_dict(orient="records")
    
else:
    to_learn = dataframe.to_dict(orient="records")

def next_card():
    global current_card, timer

    window.after_cancel(timer)
    canvas.itemconfig(canvas_img, image=front_img)
    current_card = random.choice(to_learn)
    current_card_french = current_card["French"]
    current_card_english = current_card["English"]
    canvas.itemconfig(language_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=current_card_french, fill="black")
    timer = window.after(3000, flip)


# ---------------------------- FLIPPING THE CARDS ------------------------------- #

def flip():  
    canvas.itemconfig(canvas_img, image=bg_img)
    canvas.itemconfig(language_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=current_card["English"], fill="white")


# ---------------------------- CHECK IF KNOWS WORD ------------------------------- #

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("Day-31-capstone/data/words_to_learn.csv", index=False)


    next_card()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flesh Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img = PhotoImage(file="Day-31-capstone/images/card_back.png")
front_img = PhotoImage(file="Day-31-capstone/images/card_front.png")
right_btn_img = PhotoImage(file="Day-31-capstone/images/right.png")
wrong_btn_img = PhotoImage(file="Day-31-capstone/images/wrong.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
language_txt = canvas.create_text(400, 125, text="Title", font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_btn_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_btn_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()