from turtle import Turtle, Screen
import pandas

#Configuramos la pantalla con el titulo y el fondo
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t = Turtle(image)

#creamos la tortuga que va a escribir los estados en el mapa
draw = Turtle()
draw.hideturtle()
draw.penup()
#defino el escribir de la tortuga asi solamente le paso el estado como argumento
def draw_write(state, xcor, ycor):
    draw.goto(xcor, ycor)
    draw.write(arg=state, align="center", font=("Arial", 8, "normal"))

#vamos a trabajar con pandas
data = pandas.read_csv("50_states.csv")

count_textinput = 0
while True :
#creamos la pregunta
    answer_state = screen.textinput(title="guess the state", prompt="type state name:")
    #paso la serie a lista para comprobar la respuesta con un if
    state_list = data.state.to_list()

    if answer_state.capitalize() in state_list:
        print("correcto")
        row_state = data[data["state"] == answer_state.capitalize()]
        print(row_state.x)
        print(row_state.state)
        print(row_state.y)
    else:
        print("incorrecto")

screen.exitonclick()