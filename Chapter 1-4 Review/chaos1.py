# c4_chaos.py
# Tony Chen

from graphics import *
from time import *

def main():
    print("This program illustrates 3 versions of a chaotic function.")
    print("You will see the output in a window, with a different color.")
    print("used for each version of the function.")

    print()

    yOriginal = float(input("Enter a number between 0 and 1: "))

    win = GraphWin("chaos.py", 400, 300)
    win.setCoords(0, 0, 100, 1)

    y = yOriginal

    for i in range(100):
        yNew = 3.9 * y * (1 - y)
        
        n = Line(Point(i, y), Point((i + 1), yNew))
        n.setOutline("blue")
        n.draw(win)
        
        y = yNew

        sleep(0.01)

    y = yOriginal

    for i in range(100):
        yNew = 3.9 * (y - y * y)
        
        n = Line(Point(i, y), Point((i + 1), yNew))
        n.setOutline("orange")
        n.draw(win)
        
        y = yNew

        sleep(0.01)

    y = yOriginal

    for i in range(100):
        yNew = 3.9 * y - 3.9 * y * y
        
        n = Line(Point(i, y), Point((i + 1), yNew))
        n.setOutline("darkgreen")
        n.draw(win)
        
        y = yNew

        sleep(0.01)

    p = win.getMouse()

    x = p.getX()
    
    Line(Point(x, 0), Point(x, 1)).draw(win)

    print()

    print("You clicked at x =", round(x, 0))

    win.getMouse()
    win.close()

main()
