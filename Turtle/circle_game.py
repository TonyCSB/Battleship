# circle_game.py
# Tony Chen

from turtle import *
from random import randrange
from graphics import color_rgb
FRAMES_PER_SECOND = 10

def turnRight():
    global turtle

    turtle.right(45)

def turnLeft():
    global turtle

    turtle.left(45)

def move():
    global turtle
    global mirrorTurtle
    global moving

    if moving:
        r, g, b = randomColor()
        
        turtle.forward(20)
        turtle.dot(10, color_rgb(r, g, b))
        
        mirrorTurtle.setpos(-turtle.xcor(), -turtle.ycor())
        mirrorTurtle.dot(5, color_rgb(r, g, b))
        
        ontimer(move, 1000 // FRAMES_PER_SECOND)

def start():
    global moving

    moving = True
    move()

def stop():
    global moving

    moving = False

def randomColor():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    return r, g, b

def main():
    global turtle
    global mirrorTurtle

    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()

    mirrorTurtle = Turtle()
    mirrorTurtle.hideturtle()
    mirrorTurtle.penup()

    onkey(turnRight, "Right")
    onkey(turnLeft, "Left")
    onkey(start, "Up")
    onkey(stop, "Down")
    listen()

if __name__ == "__main__":
    main()
