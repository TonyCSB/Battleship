# random_star.py
# Tony Chen

from random import randrange
from turtle import Turtle, colormode

MAX_ANGLE = 30

def jaggedLine(turtle, pieces, pieceLength):
    randomColor(turtle)
    
    for i in range(pieces):
        turtle.forward(pieceLength)
        r = randrange(-MAX_ANGLE, MAX_ANGLE + 1)
        turtle.right(r)

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
    
    jaggedLine(t, 10, 30)
    jumpToCenter(t)
    jaggedLine(t, 10, 30)

if __name__ == "__main__":
    main()
