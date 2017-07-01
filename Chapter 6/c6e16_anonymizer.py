# c6e16_anonymizer.py
# Tony Chen

from graphics import *
from math import *

def drawFace(center, size, win):
    x, y = center.getX(), center.getY()
    
    face = Circle(center, size)
    face.setWidth(1.5 * size)
    face.setOutline("Orange")
    face.setFill("Yellow")
    face.draw(win)

    mouth1 = Circle(center, 0.75 * size)
    mouth1.setFill("Brown")
    mouth1.setWidth(0)
    mouth1.draw(win)

    mouth2 = Oval(Point(-0.9 * size, -0.4 * size),
                  Point(0.9 * size, 0.4 * size))
    mouth2.setFill("Yellow")
    mouth2.setWidth(0)
    mouth2.move(x, y)
    mouth2.draw(win)

    cover1 = Rectangle(Point(-0.75 * size, 0.1 * size),
                       Point(0.75 * size, 0.5 * size))
    cover1.setFill("Yellow")
    cover1.setWidth(0)
    cover1.move(x, y)
    cover1.draw(win)

    cover2 = Rectangle(Point(-0.6 * size, 0.5 * size),
                       Point(0.6 * size, 0.7 * size))
    cover2.setFill("Yellow")
    cover2.setWidth(0)
    cover2.move(x, y)
    cover2.draw(win)

    cover3 = Rectangle(Point(-0.3 * size, 0.7 * size),
                       Point(0.3 * size, 0.8 * size))
    cover3.setFill("Yellow")
    cover3.setWidth(0)
    cover3.move(x, y)
    cover3.draw(win)
    
    eyeWidth = 0.3 * size
    eyeHeight = 0.4 * size

    eyeLeft = 0.125 * size
    eyeUp = 0.1 * size

    eye1 = Oval(Point(-eyeWidth - eyeLeft, eyeUp), Point(-eyeLeft, eyeUp + eyeHeight))
    eye1.setWidth(1.5 * size)
    eye1.setFill("Brown")
    eye1.setOutline("Sandy Brown")
    eye1.move(x, y)
    eye1.draw(win)

    eye2 = Oval.clone(eye1)
    eye2.move(eyeWidth + 2 * eyeLeft, 0)
    eye2.draw(win)

    noseCenter = Point(x, y - 0.05 * size)
    nose = Circle(noseCenter, 0.05 * size)
    nose.setFill("Brown")
    nose.setWidth(0)
    nose.draw(win)

def distance(p1, p2):
    d = sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    return d

def main():
    print("This program allows you to draw a cartoon face on the picture.\n")

    infileName = input("Picture file name? ")

    image = Image(Point(0, 0), infileName)

    x = image.getWidth()
    y = image.getHeight()

    win = GraphWin("Anonymizer.py", x, y)
    win.setCoords(-10, -10, 10, 10)

    image.draw(win)

    n = int(input("How many faces are to be blocked? "))

    for i in range(n):
        center = win.getMouse()
        p2 = win.getMouse()
        size = distance(center, p2)
        drawFace(center, size, win)

main()
    
