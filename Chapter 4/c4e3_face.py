# c4e3_face.py
# Tony Chen

from graphics import *

def main():
    win = GraphWin("FACE!", 500, 500)
    win.setCoords(-2.5, -2.5, 2.5, 2.5)

    center = Point(0, 0)

    faceOutline1 = Circle(center, 2.3)
    faceOutline1.setFill("Orange")
    faceOutline1.setWidth(0)
    faceOutline1.draw(win)

    faceOutline2 = Circle(center, 2)
    faceOutline2.setFill("Yellow")
    faceOutline2.setWidth(0)
    faceOutline2.draw(win)

    mouth1 = Circle(center, 1.5)
    mouth1.setFill("Brown")
    mouth1.setWidth(0)
    mouth1.draw(win)

    mouth2 = Oval(Point(-2, -0.8), Point(2, 0.8))
    mouth2.setFill("Yellow")
    mouth2.setWidth(0)
    mouth2.draw(win)

    cover1 = Rectangle(Point(-1.384, -0.577), Point(1.384, 1.2))
    cover1.setFill("Yellow")
    cover1.setWidth(0)
    cover1.draw(win)

    cover2 = Rectangle(Point(-1, 1.2), Point(1, 1.5))
    cover2.setFill("Yellow")
    cover2.setWidth(0)
    cover2.draw(win)

    eye1 = Oval(Point(-0.8, 0.2), Point(-0.2, 1))
    eye1.setWidth(5)
    eye1.setOutline("Sandy Brown")
    eye1.setFill("Brown")
    eye1.draw(win)

    eye2 = Oval.clone(eye1)
    eye2.move(1, 0)
    eye2.draw(win)

    nose = Circle(Point(0, -0.1), 0.1)
    nose.setFill("Brown")
    nose.setWidth(0)
    nose.draw(win)

    
main()
