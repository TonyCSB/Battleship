# c4e8_line.py
# Tony Chen

from graphics import *
from math import *

def main():
    win = GraphWin("c4e8_line.py", 600, 400)
    win.setCoords(-15, -10, 15, 10)

    text = Text(Point(0, 0),
                "This program allows the user to draw a line segment\n"+
                "and then displays some graphical and textual information\n"+
                "about the line segment.\n"+
                "\n"+
                "(Click to continue.)")
    text.draw(win)

    win.getMouse()
    text.undraw()

    text.setText(
        "Click on two different points within the screen\n"+
        "to define the two end points of the line segment.")
    text.draw(win)

    a = win.getMouse()

    text.undraw()

    aPoint = Circle(a, 0.3)
    aPoint.setOutline("red")
    aPoint.setWidth(2)
    aPoint.draw(win)

    b = win.getMouse()

    bPoint = Circle(b, 0.3)
    bPoint.setOutline("red")
    bPoint.setWidth(2)
    bPoint.draw(win)

    line = Line(a, b)
    line.setOutline("Blue")
    line.setWidth(3)
    line.draw(win)

    x1 = a.getX()
    x2 = b.getX()
    y1 = a.getY()
    y2 = b.getY()

    midX = (x1 + x2) / 2
    midY = (y1 + y2) / 2

    midPoint = Circle(Point(midX, midY), 0.3)
    midPoint.setOutline("Cyan")
    midPoint.setWidth(2)
    midPoint.draw(win)

    Text(Point(midX, midY + 1.5), "midpoint").draw(win)

    length = sqrt((x2 - x1) ** 2+(y2 - y1) ** 2)

    slope = (y2 - y1) / (x2 - x1)

    text.setText("The length of the line is " + str(round(length, 2)) + ".\n" +
              "\n" +
              "The slope of the line is " + str(round(slope, 2)) + ".")

    text.draw(win)

    win.getMouse()
    win.close()

main()
