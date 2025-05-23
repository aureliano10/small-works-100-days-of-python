try:
    age = int(input("How old are you?"))
except ValueError:
    "haz colocado un valor invalido prueba de nuevo"
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
