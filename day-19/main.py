from turtle import Turtle, Screen
import random

tom = Turtle(shape= "turtle")
tim = Turtle(shape= "turtle")
tam = Turtle(shape= "turtle")
tum = Turtle(shape= "turtle")
tem = Turtle(shape= "turtle")
dam = Turtle(shape= "turtle")

screen = Screen()
screen.setup(width=500, height=400)

turtles = [tom, tim, tam, tum, tem, dam]
colors = ["blue", "green", "red", "orange", "purple", "yellow"]
count = 0
y_count = -150
for t in turtles:
    t.color(colors[count])
    t.penup()
    t.goto(x= -230, y= y_count)
    y_count += 50
    count += 1

is_race_on = False
user_bet = screen.textinput(title= "make your bet", prompt= "what turtle winner the race?: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        random_number = random.randint(0, 10)
        t.forward(random_number)
        if t.xcor() >= 230:
            print(f"The turtle winner is: {t.color()[0]}")
            if user_bet == t.color()[0]:
                print("you win the bet")
            else:
                print("you wrong the bet")

            is_race_on = False
            break

screen.exitonclick()


