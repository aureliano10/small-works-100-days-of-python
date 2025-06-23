import tkinter as tk


#creo una ventana con tkinter
window = tk.Tk()

#le ponemos titulo a la ventana
window.title("mi primer GUI")

#le damos un tamaño minimo aunque podría ser más grande dependiendo del contenido que tenga
window.minsize(width= 700, height= 400)

#Establecemos padding para los bordes de la ventana
window.config(padx=80, pady=80)

#LABEL(etiqueta)
# crear una etiqueta y almacenarla en una variable
my_label = tk.Label(text="Mi primera etiqueta", font=("Arial", 27, "bold"))
#hacemos que se muestre en la pantalla y justo en el centro arriba(por defecto) con .pack
my_label.grid(column= 0, row=0)
#CAMBIAR PROPIEDADES
my_label["text"] = "Probando probando"
my_label.config(text="text2")

#BUTTON(boton)
# def button_clicked():
#     my_label["text"] = "I got clicked"
#     # print("me hicieron click(i got clicked)")

def new_button_clicked():
    my_label["text"] = input_text.get()

my_button = tk.Button(text= "Click Me", command=new_button_clicked)
my_button.grid(column=1, row=1)

new_button = tk.Button(text="New button")
new_button.grid(column=3, row=0)

input_text = tk.Entry(width=20)
input_text.grid(column=4, row=2)


#esta función mantiene la pantalla, es como si fuera un bucle while
window.mainloop()
