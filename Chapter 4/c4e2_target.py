# c4e2_target.py
# Tony Chen

from graphics import *

def main():
    win = GraphWin("Target")
    win.setCoords(-5.5, -5.5, 5.5, 5.5)

    radius = 1
    center = Point(0,0)

    whiteRing = Circle(center, radius * 5)
    whiteRing.setFill("white")
    whiteRing.draw(win)

    blackRing = Circle(center, radius * 4)
    blackRing.setFill("black")
    blackRing.draw(win)

    blueRing = Circle(center, radius * 3)
    blueRing.setFill("blue")
    blueRing.draw(win)

    redRing = Circle(center, radius * 2)
    redRing.setFill("red")
    redRing.draw(win)

    yellowRing = Circle(center, radius)
    yellowRing.setFill("yellow")
    yellowRing.draw(win)

    win.getMouse()
    win.close()

main()
