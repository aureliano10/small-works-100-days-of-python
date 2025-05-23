from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("darkviolet")
my_screen = Screen()

print(my_screen.canvheight)
timmy.forward(100)
my_screen.bgcolor("red")
my_screen.exitonclick()
