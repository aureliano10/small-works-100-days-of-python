import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw_char = []
for i in range(nr_letters):
    pw_char += random.choice(letters)

for i in range(nr_symbols):
    pw_char += random.choice(symbols)

for i in range(nr_letters):
    pw_char += random.choice(numbers)

#easy
easy_password = pw_char
password_easy = ""
for items in easy_password:
    password_easy += items
print(password_easy)

#hard
user_password_hard = pw_char
random.shuffle(user_password_hard) #esto mezcla los elementos de una lista
password = ""
for items in user_password_hard:  #aca iteramos sobre cada item de la var user_password_hard i los almacena como una cadena en la variable password
    password += items
print(f"your password is: {password}")