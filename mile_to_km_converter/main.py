import tkinter as tk

window = tk.Tk()
window.minsize(width=100, height=100)
window.title("Mile to km converter")
window.config(pady= 20, padx= 10)

label_text_is_equal_to = tk.Label(text="Is equal to")
label_text_is_equal_to.grid(column=0, row=1)

miles_input = tk.Spinbox()
miles_input.grid(column= 1, row= 0)

km_converted = tk.Label(text= "0")
km_converted.grid(column= 1, row=1)

def calculate_km():
    text_in_window = int(miles_input.get()) * 1.60934
    km_converted["text"] = round(text_in_window, 1)

button_calculate = tk.Button(text="Calculate", command= calculate_km)
button_calculate.grid(column= 1, row= 2)

label_text_miles = tk.Label(text="Miles")
label_text_miles.grid(column= 2, row= 0)

label_text_km = tk.Label(text="Km")
label_text_km.grid(column= 2, row= 1)



window.mainloop()