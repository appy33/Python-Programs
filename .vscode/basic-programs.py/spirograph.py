
import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0.18)
for i in range(6):
  for colours in ["red", "magenta", "white", "yellow", "blue", "cyan", "green"]:
    turtle.color(colours)
    turtle.circle(100)
    turtle.left(100)
turtle.hideturtle()




