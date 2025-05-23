import random
from art import logo

def user_health(difficult):
    """
    establece las vidas del jugador en base a la dificultad
    """
    if difficult == 0:
        return 10
    else:
        return 5


def guess_the_number():
    print(logo)

    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    level = user_health(int(input("chose your difficult\nEasy = 0\nHard = 1\nType 0 or 1: ")))

    number_guess = random.randint(1, 100)

    print(f"You have {level} attempts")

    guess_user = False
    while not guess_user:
        if level == 0:
            print("You lose")
            guess_user = True
        else:
            user_number = int(input("Make a guess: "))
            if user_number == number_guess:
                print(f"You got it, the answer is {number_guess}")
                guess_user = True
            elif user_number > number_guess:
                print("Too high")
                level -= 1
                print(f"You have {level} attempts")
            else:
                print("Too low")
                level -= 1
                print(f"You have {level} attempts")

    while input("Do you play again? type 'y' or 'n'") == "y":
        print("\n" * 20)
        guess_the_number()

guess_the_number()