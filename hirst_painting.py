import turtle as t
import random

oogway = t.Turtle()
t.colormode(255)


def Rand_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def go(x, y):
    oogway.penup()
    oogway.goto(x, y)
    oogway.pendown


x = -350
y = -350
oogway.speed(0)

for j in range(10):
    for i in range(10):
        go(x, y)
        oogway.color(Rand_colour())
        oogway.begin_fill()
        oogway.circle(10)
        oogway.end_fill()
        x += 70
    x = -350
    y += 70

oogway.hideturtle()

screen = t.Screen()
screen.exitonclick()
