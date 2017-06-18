# c4e10_triangle.py
# Tony Chen

from graphics import *
from math import *

def main():
    win = GraphWin("c4e10_triangle.py", 600, 400)
    win.setCoords(-15, -10, 15, 10)

    text = Text(Point(0, 0),
                "This program displays information about\n" +
                "a triangle drawn by the user.\n" +
                "\n" +
                "(Click to continue.)")
    text.draw(win)

    win.getMouse()
    text.undraw()

    text.setText("Please click on the screen three times\n" +
                 "to determine the vertices of a triangle.")
    text.draw(win)

    a = win.getMouse()
    aPoint = Circle(a, 0.3)
    aPoint.setOutline("Red")
    aPoint.draw(win)
    text.undraw()

    b = win.getMouse()
    bPoint = Circle(b, 0.3)
    bPoint.setOutline("Red")
    bPoint.draw(win)

    c = win.getMouse()
    cPoint = Circle(c, 0.3)
    cPoint.setOutline("Red")
    cPoint.draw(win)

    Polygon(a, b, c).draw(win)

    x1, x2, x3 = a.getX(), b.getX(), c.getX()
    y1, y2, y3 = a.getY(), b.getY(), c.getY()

    ab = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    bc = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    ac = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

    s = (ab + bc + ac) / 2

    area = sqrt(s * (s - ab) * (s - ac) * (s - bc))
    perimeter = 2 * s

    text.setText("The perimeter of the triangle is " +
                 str(round(perimeter, 2)) + ".\n" +
                 "The area of the triangle is " +
                 str(round(area, 2)) + ".")
    text.draw(win)

    win.getMouse()
    win.close()

main()
