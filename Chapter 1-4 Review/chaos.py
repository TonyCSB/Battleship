# chaos.py
# Tony Chen

from graphics import *
from time import *

def main():
    win = GraphWin("CHAOS!", 500, 500)
    win.setCoords(-10, -10, 10, 10)

    text = Text(Point(0, 0),
                "This program illustrates the chaotic behavior.\n" +
                "\n" +
                "(Click to continue.)")
    text.draw(win)

    win.getMouse()
    text.undraw()

    aText = Text(Point(0, 3),"Please enter one number between 0 and 1:")
    aText.draw(win)


    bText = Text(Point(0, -1), "Please enter another number between 0 and 1:")
    bText.draw(win)

    bNumber = Entry(Point(0, -3), 5)
    bNumber.draw(win)
    
    aNumber = Entry(Point(0, 1), 5)
    aNumber.draw(win)
    
    text1 = Text(Point(0, 9), "(Click anywhere to continue.)")
    text1.draw(win)

    win.getMouse()
    aText.undraw()
    bText.undraw()
    aNumber.undraw()
    bNumber.undraw()
    text1.undraw()

    aNumber = round(float(aNumber.getText()), 2)
    bNumber = round(float(bNumber.getText()), 2)

    xAxis = Line(Point(-8.5, -9.0), Point(-8.5, 8.5))
    xAxis.setArrow("last")
    xAxis.draw(win)

    yAxis = Line(Point(-9.0, -8.5), Point(8.5, -8.5))
    yAxis.setArrow("last")
    yAxis.draw(win)

    for i in range (11):
        x = -9.3
        y = 1.65 * x - 8.5
        Text(Point(x, y), 10000).draw(win)

    win.getMouse()
    win.close    

main()
