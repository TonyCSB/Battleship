# c4e9_rectangle.py
# Tony Chen

from graphics import *

def main():
    win = GraphWin("c4e9_rectangle.py", 600, 400)
    win.setCoords(-15, -10, 15, 10)

    text = Text(Point(0, 0),
                "This program displays information about a\n" +
                "rectangle drawn by the user.\n" +
                "\n" +
                "(Click to continue.)")
    text.draw(win)

    win.getMouse()
    text.undraw()

    text.setText(
        "Click on the screen twice to determine the opposite corners\n" +
        "of the rectangle.")
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

    Rectangle(a, b).draw(win)

    x1, x2 = a.getX(), b.getX()
    y1, y2 = a.getY(), b.getY()

    length = abs(x1 - x2)
    width = abs(y1 - y2)

    area = length * width
    perimeter = 2 * (length + width)

    text.setText(
        "The area of the rectangle is " + str(round(area, 2)) + ".\n" +
        "The perimeter of the rectangle is " +
        str(round(perimeter, 2)) + ".")
    text.draw(win)

    win.getMouse()
    win.close()

main()
