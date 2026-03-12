import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    label_check_mark.config(text="")
    label_timer.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """Number in minutes"""
    global reps
    reps += 1
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        label_timer.config(text="Long Break", fg= RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        label_timer.config(text="Work",fg= GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        label_timer.config(text="Short Break", fg= PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if count == 0:
        if reps % 2 == 0:
            label_check_mark.config(text= "✔" * (reps // 2))
        start_timer()
    else:
        minutes = math.floor(count / 60)
        seconds = round(count % 60)

        if seconds < 10:
            seconds = f"0{seconds}"
        if minutes < 10:
            minutes = f"0{minutes}"

        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
        global timer
        timer = window.after(1000, count_down, count -1)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)





canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#creamos una imagen fotografica para poder usarla en create_image
image_tomato = tk.PhotoImage(file = "tomato.png")

#Creamos el canvas de imagen
#Los dos primeros valores son las coordenadas x, y
canvas.create_image(100, 112, image= image_tomato)

#Creamos el canvas de texto
timer_text = canvas.create_text(100, 130 , text= "00:00", fill="White", font=(FONT_NAME, 25, "bold"))

#se empaqueta para mostrarse en la pantalla
canvas.grid(column= 1, row= 1)

button_start = tk.Button(text="Start", command= start_timer)
button_start.grid(column= 0, row= 2)

button_restart = tk.Button(text="Restart", command=reset_timer)
button_restart.grid(column= 2, row= 2)

label_timer = tk.Label(fg=GREEN, text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW)
label_timer.grid(column= 1, row= 0)


label_check_mark = tk.Label(fg=GREEN, bg= YELLOW, font= (FONT_NAME, 30, "bold"))
label_check_mark.grid(column= 1, row= 3)

window.mainloop()