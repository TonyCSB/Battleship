# c7e16_archery.py
# Tony Chen

from graphics import *
import math

def target(win):
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

def distance(p1, p2):
    d = math.sqrt((p1.getX() - p2.getX()) ** 2 +
                  (p1.getY() - p2.getY()) ** 2)
    return d

def main():
    print("This program draws an archery target and allows")
    print("the user to click five times to represent arrows")
    print("shot at the target.\n")

    input("Press <Enter> to contine.")

    win = GraphWin("Target")
    win.setCoords(-5.5, -5.5, 5.5, 5.5)
    
    target(win)

    print("\n        Score    Sum   ")

    sumScore = 0

    for i in range(5):
        a = win.getMouse()
        d = distance(a, Point(0, 0))

        score = -2 * int(d) + 9
        sumScore = sumScore + score

        print("   {0}     {1}        {2}  ".format(i + 1, score, sumScore))

    try:
        win.getMouse()
        win.close()
        
    except:
        pass

if __name__ == "__main__":
    main()
