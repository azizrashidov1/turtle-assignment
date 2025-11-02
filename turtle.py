import turtle
import colorsys

az = turtle.Turtle()
az.speed(300)
az.speed(0)
turtle.bgcolor("black")
az.width(2)

n = 36
h = 0

for i in range(240):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    az.pencolor(c)
    az.circle(100)
    az.right(10)
    az.forward(10)
    h += 1/n

az.pencolor("white")
az.write(" Hello", align="left", font=("Arial", 24, "bold"))

az.hideturtle()
turtle.done()
