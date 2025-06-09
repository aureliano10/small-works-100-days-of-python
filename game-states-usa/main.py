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
def draw_write(state):
    draw.write(arg=state, align="center", font=("Arial", 8, "normal"))

#vamos a trabajar con pandas
data = pandas

#creamos la pregunta
answer_state = screen.textinput(title="guess the state", prompt="type state name:")


screen.exitonclick()