print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_input1 = input("escoge entre izquierda(i) o derecha(d)\n").lower()
if user_input1 == "d" or user_input1 == "derecha":
    print("te has topado con un oso. haz muerto..")
elif user_input1 == "i" or user_input1 == "izquierda":
    print("haz elegido el camino correcto, avanzas hasta la gran montaña")
    user_input2 = input("elige entre escalar(e) o rodear(r) la montaña\n").lower()
    if user_input2 == "e" or user_input2 == "escalar":
        print("llegas hasta la cima")
        user_input3 = input("tienes tres cofres A, B o C, escoge uno\n").lower()
        if user_input3 == "a":
            print("haz encontrado el tesoro")
        elif user_input3 == "b":
            print("el tesoro explota, perdiste")
        elif user_input3 == "c":
            print("el tesoro explota, perdiste")
        else:
            print("opcion no valida")
    elif user_input2 == "r"or user_input2 == "rodear":
        print("encontraste un puma y te ha atacado, perdiste")
    else:
        print("opcion no valida")
else:
    print("opcion no valida")