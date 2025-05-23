import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_value = int(input("escribe 0 para piedra, escribe 1 para papel, escribe 2 para tijeras\n"))
if user_value > 3:
    print("escogiste un valor incorrecto, perdiste")
else:
    print("escogiste: ")
    print(game_images[user_value])
    '''
    if user_value == 1:
        print(game_images[user_value])
    elif user_value == 2:
        print(game_images[user_value])
    else:
        print(game_images[user_value])
    '''
    pc_value = random.randint(0, 2)

    print("computadora elige: ")

    print(game_images[pc_value])
    '''
    if pc_value == 0:
        print(game_images[pc_value])
    elif pc_value == 1:
        print(game_images[pc_value])
    else:
        print(game_images[pc_value])
    '''
    if pc_value == user_value:
        print("empate")
    elif pc_value == 0 and user_value == 3:
        print("gana la computadora")
    elif pc_value == 1 and user_value == 1:
        print("gana la computadora")
    elif pc_value == 2 and user_value == 2:
        print("gana la computadora")
    else:
        print("has ganado")