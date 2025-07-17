import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

label_timer = tk.Label(fg=GREEN, text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW)
label_timer.grid(column= 1, row= 0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#creamos una imagen fotografica para poder usarla en create_image
image_tomato = tk.PhotoImage(file = "tomato.png")

#Creamos el canvas de imagen
#Los dos primeros valores son las coordenadas x, y
canvas.create_image(100, 112, image= image_tomato)

#Creamos el canvas de texto
canvas.create_text(100, 130 , text= "00:00", fill="White", font=(FONT_NAME, 25, "bold"))

#se empaqueta para mostrarse en la pantalla
canvas.grid(column= 1, row= 1)

button_start = tk.Button(text="Start")
button_start.grid(column= 0, row= 2)

button_restart = tk.Button(text="Restart")
button_restart.grid(column= 2, row= 2)

#Este es el recuento de ciclos de pomodoro
pomodoro_count = 3

label_check_mark = tk.Label(text= "✔" * pomodoro_count, fg=GREEN, bg= YELLOW, font= (FONT_NAME, 30, "bold"))
label_check_mark.grid(column= 1, row= 3)

window.mainloop()