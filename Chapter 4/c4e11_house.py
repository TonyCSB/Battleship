# c4e11_house.py
# Tony Chen

from graphics import *

def main():
    win = GraphWin("c4e11_house.py", 600, 400)
    win.setCoords(-15, -10, 15, 10)

    text = Text(Point(0, 0),
                "This program allows you to draw a simple house\n" +
                "using five mouse clicks.\n" +
                "\n" +
                "(Click to continue.)")
    text.draw(win)

    win.getMouse()
    text.undraw()

    text = Text(Point(0, 8),
                "Please click twice within the screen to indicate the\n" +
                "opposite corners of the rectangular frame of the house.")
    text.draw(win)

    a = win.getMouse()
    a.draw(win)
    b = win.getMouse()
    a.undraw()

    house = Rectangle(a, b)
    house.draw(win)

    aX, bX = a.getX(), b.getX()
    aY, bY = a.getY(), b.getY()

    houseLength = abs(aX - bX)

    halfDoorLength = 1 / 10 * houseLength

    text.setText("Please click within the house to indicate\n" +
                 "the center of the top edge of the rectangular door.")
    c = win.getMouse()
    cX, cY = c.getX(), c.getY()

    c1 = Point(cX - halfDoorLength, aY)
    c2 = Point(cX + halfDoorLength, cY)

    door = Rectangle(c1, c2)
    door.draw(win)

    text.setText("Please click within the house to indicate\n" +
                 "the center of a square window.")

    d = win.getMouse()
    
    dX, dY = d.getX(), d.getY()

    halfWindowLength = 1 / 2 * halfDoorLength

    d1 = Point(dX - halfWindowLength, dY - halfWindowLength)
    d2 = Point(dX + halfWindowLength, dY + halfWindowLength)

    window = Rectangle(d1, d2)
    window.draw(win)

    text.setText("Please click again above the house to indicate\n" +
                 "the peak of the roof")

    e = win.getMouse()

    roof = Polygon(e, b, Point(aX, bY))
    roof.draw(win)

    text.setText("Click to exit.")

    win.getMouse()
    win.close()

main()
