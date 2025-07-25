import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    data_frame = pandas.read_csv("data/data_words_traduction.csv")

finally:
    #pasamos a diccionario con claves pares y valor por cada fila
    to_dict = data_frame.to_dict(orient="records")

new_card = ""
def next_card():
    global new_card, flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(to_dict)
    canvas.itemconfig(text_word, text=new_card["English"], fill= "black")
    canvas.itemconfig(title_word, text="English", fill= "black")
    canvas.itemconfig(image_card, image=image_front)
    flip_timer = window.after(3000, flip_card)

def delete_element():
    to_dict.remove(new_card)

def flip_card():
    canvas.itemconfig(image_card, image=image_back)
    canvas.itemconfig(title_word, text="Spanish", fill="white")
    canvas.itemconfig(text_word, text=new_card["Spanish"], fill="white")

def right_button_pressed():
    delete_element()
    data = pandas.DataFrame(to_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# def wrong_button_pressed():
#     delete_element()
#     next_card()

#---------------------------ventana------------------#
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
#------------------Creacion de GUI-----------------------#

canvas = tk.Canvas(width= 810, height= 530, bg=BACKGROUND_COLOR, highlightthickness=0)

#----------configuracion de imagenes
image_front = tk.PhotoImage(file= "images/card_front.png")
image_back = tk.PhotoImage(file= "images/card_back.png")
image_wrong = tk.PhotoImage(file= "images/wrong.png")
image_right = tk.PhotoImage(file= "images/right.png")

#--------Crear la imagen de tarjeta
image_card = canvas.create_image(410, 268, image= image_front)
canvas.grid(column=0, row=0, columnspan=2)
title_word = canvas.create_text(400, 150, text="", font= ("Arial", 40, "italic"))
text_word = canvas.create_text(400, 268, text="", font= ("Arial", 60, "bold"))

#--------Crear los botones
button_wrong = tk.Button(image=image_wrong, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(column=0, row=1)

button_right = tk.Button(image=image_right, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=right_button_pressed)
button_right.grid(column=1, row=1)


next_card()

window.mainloop()