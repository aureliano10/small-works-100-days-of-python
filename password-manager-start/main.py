import tkinter as tk
from tkinter import messagebox
import random
import json

FONT= ("Arial", 10, "normal")

# ---------------------------- Search Password ----------------------------------#

def search_password():
    website = input_website.get()
    if len(website) <= 0:
        messagebox.showinfo(title= "Error", message= "Please enter a word")

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Passwords", message="Your password list is empty")
    else:
        try:
            website_data = data[website]
            messagebox.showinfo(title="Passwords", message=f"Email: {website_data["email"]}\n"
                                                           f"Password: {website_data["password"]}")
        except KeyError:
            messagebox.showinfo(title="Passwords", message=f"There is not passdword for: '{website}'")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pwd_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    pwd_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = pwd_letters + pwd_numbers + pwd_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    input_password.delete(0, "end")
    input_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    """Guardar datos"""
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "" or email == "":
        messagebox.showinfo(title="Error", message="Complete the fields")

    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message= f"save your data?\n"
                                                                     f"email: {email}\n"
                                                                     f"password: {password}")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # file.write(f"{web_site} | {email} | {password} \n")
                    # #--cargar datos json
                    # json.dump(new_data, file, indent= 4)
                    #--leer datos json
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                #--en caso de no estar inicializado el data.json
                #--esta-es-una-solucion
                #data = {}
                #--esta-es-otra
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent= 4)
            else:
                #--actualizar datos json
                data.update(new_data)

                #--cargo los datos
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                input_website.delete(0, "end")
                input_password.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.minsize(200, 200)
window.config(padx=50, pady=50)

logo_img = tk.PhotoImage(file = "logo.png")

canvas = tk.Canvas(width=200, height=200)

canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

label_text_website = tk.Label(text="Website:", font=FONT)
label_text_website.grid(column=0, row=1)

label_text_email = tk.Label(text="Email/Username:", font= FONT)
label_text_email.grid(column=0, row=2)

label_text_password = tk.Label(text = "Password:", font=FONT)
label_text_password.grid(column=0, row= 3)

input_website = tk.Entry(width=21)
input_website.grid(column=1, row=1)

#la funcion focus coloca el cursor en esa posicion
input_website.focus()

button_search = tk.Button(text="Search", width=14, command= search_password)
button_search.grid(column=2, row=1)

input_email = tk.Entry(width=38)
input_email.grid(column= 1, row= 2,columnspan= 2)

#La funcion insert toma dos parametros (indice, string)
input_email.insert(0, "eichhornaureliano@gmail.com")

input_password = tk.Entry(width=21)
input_password.grid(column=1, row=3)

button_generate_password = tk.Button(text="Generate Password", width=14, command= generate_password)
button_generate_password.grid(column=2, row=3)

button_add = tk.Button(text="Add", width=36, command= save_data)
button_add.grid(column=1, row=4,columnspan=2)

window.mainloop()