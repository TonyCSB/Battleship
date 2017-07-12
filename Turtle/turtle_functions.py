# turtle_functions.py
# Tony Chen

from turtle import *

def square(turtle, sideLength):

    for i in range(4):
        turtle.forward(sideLength)
        turtle.right(90)

def triangle(turtle, sideLength):

    for i in range (3):
        turtle.forward(sideLength)
        turtle.right(120)

def polygon(turtle, sideLength, numSides):

    angle = 360 / numSides

    for i in range(numSides):
        turtle.forward(sideLength)
        turtle.right(angle)

def polygonStar(turtle, sideLength, numSides, numPolygons):

    for i in range(numPolygons):
        polygon(turtle, sideLength, numSides)
        turtle.right(360 / numPolygons)

def main():
    t = Turtle()
    t.reset()
    #square(t, 100)
    #triangle(t, 100)
    #polygon(t, 100, 10)
    polygonStar(t, 100, 9, 20)

if __name__ == "__main__":
    main()
