# random_star.py
# Tony Chen

from random import randrange
from turtle import Turtle, colormode
from math import sqrt

MAX_ANGLE = 30

def jaggedLine(turtle, length, pieceLength):
    randomColor(turtle)

    while distance(turtle) < length:
        turtle.forward(pieceLength)
        r = randrange(-MAX_ANGLE, MAX_ANGLE + 1)
        turtle.right(r)

def distance(turtle):
    x, y = turtle.xcor(), turtle.ycor()
    distance = sqrt(x ** 2 + y ** 2)
    return distance

def jumpToCenter(turtle):
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()

def randomColor(turtle):
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)

    turtle.pencolor(r, g, b)

def main():
    colormode(255)
    t = Turtle()
    t.hideturtle()

    for i in range(100):
        jaggedLine(t, 250, 30)
        jumpToCenter(t)

if __name__ == "__main__":
    main()
