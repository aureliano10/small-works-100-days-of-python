from turtle import Turtle, Screen
import pandas

#Configuramos la pantalla con el titulo y el fondo
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t = Turtle(image)

#vamos a trabajar con pandas
data = pandas.read_csv("50_states.csv")
# paso la serie a lista para comprobar la respuesta con un if
all_states = data.state.to_list()

guessed_states = []

#stadistic_states = []
is_states_guessed = []

dict_to_csv = {}

while len(guessed_states) < 50:
    #creamos la pregunta
    answer_state = screen.textinput(title=f"guess the state--states {len(guessed_states)}/50", prompt="type state name:").title()

    if answer_state == "Exit":
        for state in all_states:
            if state in guessed_states:
                is_states_guessed.append("Guessed")
            else:
                is_states_guessed.append("Wrong")
        dict_to_csv = {
            "states" : all_states,
            "Guessed?" : is_states_guessed
        }
        new_df = pandas.DataFrame(dict_to_csv)
        new_df.to_csv("stadistic_of_game.csv")
        break


    if answer_state in all_states:
        if answer_state in guessed_states:
            print(f"{answer_state} is guessed")

        else:
            t1 = Turtle()
            t1.hideturtle()
            t1.penup()
            state_data = data[data.state == answer_state]
            t1.goto(state_data.x.item(), state_data.y.item())
            t1.write(state_data.state.item())
            guessed_states.append(answer_state)

    else:
        print(f"Wrong, {answer_state} is not a state")

screen.exitonclick()