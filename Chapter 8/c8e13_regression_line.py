# c8e13_regression_line.py
# Tony Chen

from graphics import *

def main():
    print("This program can graphically plots a regreesion line.\n")

    input("Press <Enter> to continue. ")

    win = GraphWin("Regression Line", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    rec = Rectangle(Point(-10, -10), Point(-6, -8))
    rec.draw(win)

    text = Text(Point(-8, -9), "Done")
    text.draw(win)

    a = win.getMouse()
    Circle(a, 0.1).draw(win)
    x = a.getX()
    y = a.getY()

    xSum = 0
    xSquSum = 0
    xySum = 0
    ySum = 0
    count = 0

    while True:
        xSum = xSum + x
        xSquSum = xSquSum + x ** 2
        xySum = xySum + x * y
        ySum = ySum + y
        count = count + 1

        a = win.getMouse()
        x = a.getX()
        y = a.getY()
        if not(x < -6 and y < -8):
            Circle(a, 0.1).draw(win)
        else: break
        

    text.undraw()
    rec.undraw()

    xAverage = xSum / count
    yAverage = ySum / count

    m = (xySum - count * xAverage * yAverage) / (xSquSum - count * xAverage ** 2)

    dx = 20 / 1000

    x = -10
    xOld = -10
    yOld = yAverage + m * (x - xAverage)

    for i in range(1000):
        y = yAverage + m * (x - xAverage)

        Line(Point(x, y), Point(xOld, yOld)).draw(win)

        xOld, yOld = x, y

        x = x + dx

    try:
        win.getMouse()
        win.close()
    except:
        pass

main()
