'''from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("darkviolet")
my_screen = Screen()

print(my_screen.canvheight)
timmy.speed(1)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
my_screen.bgcolor("red")
my_screen.exitonclick()'''
from unittest.mock import DEFAULT

from prettytable import PrettyTable
from prettytable import TableStyle

table = PrettyTable()
table.add_column("football players",["Messi", "Ronaldo", "Iniesta"])
table.add_column("football teams",["Liverpool", "Barcelona", "Arsenal"])
print(table)
car_table = PrettyTable()
car_table.field_names = ["Nombre", "Marca", "Modelo", "valor en USD"]
car_table.add_rows(
    [
        ["Vento", "Volkswagen", "2020", "5000"],
        ["Golf", "Volkswagen", "2018", "3000"],
        ["GT", "Nissan", "2016", "8000"],
        ["Amarok", "Volkswagen", "2021", "12000"],
    ]
)
car_table.align = "c"
car_table.set_style(TableStyle.MSWORD_FRIENDLY)
print(car_table)

