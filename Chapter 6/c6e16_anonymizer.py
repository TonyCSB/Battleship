# c6e16_anonymizer.py
# Tony Chen

from graphics import *
from math import *

def drawFace(center, size, win):
    x, y = center.getX(), center.getY()
    
    face2 = Circle(center, size * 1.15)
    face2.setWidth(0)
    face2.setFill("Orange")
    face2.draw(win)

    face1 = Circle(center, size)
    face1.setWidth(0)
    face1.setFill("Yellow")
    face1.draw(win)
    
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

    left = [0.75, 0.6, 0.3]
    down = [0.1, 0.5, 0.7]
    up = [0.5, 0.7, 0.8]

    cover(left, down, up, size, win, x, y)
    
    eyeWidth = 0.3 * size
    eyeHeight = 0.4 * size

    eyeLeft = 0.125 * size
    eyeUp = 0.1 * size

    eye1 = Oval(Point(-eyeWidth - eyeLeft, eyeUp),
                Point(-eyeLeft, eyeUp + eyeHeight))
    eye1.setWidth(0)
    eye1.setFill("Brown")
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

def cover(left, down, up, size, win, x, y):
    for i in range(len(left)):
        cover = Rectangle(Point(-left[i] * size, down[i] * size),
                          Point(left[i] * size, up[i] * size))
        cover.setFill("Yellow")
        cover.setWidth(0)
        cover.move(x, y)
        cover.draw(win)

def main():
    print("This program allows you to draw a cartoon face on the picture.\n")

    infileName = input("Picture file name?(.gif/.ppm) ")
    n = int(input("How many faces are to be blocked? "))

    image = Image(Point(0, 0), infileName)

    x = image.getWidth()
    y = image.getHeight()

    win = GraphWin("Anonymizer.py", x, y)
    win.setCoords(-x, -y, x, y)

    image.draw(win)

    for i in range(n):
        center = win.getMouse()
        centerPoint = Circle(center, 0.01 * x)
        centerPoint.setOutline("Red")
        centerPoint.setFill("Red")
        centerPoint.draw(win)
        
        p2 = win.getMouse()
        centerPoint.undraw()
        
        size = distance(center, p2)
        drawFace(center, size, win)

    win.getMouse()
    win.close()

main()
    
