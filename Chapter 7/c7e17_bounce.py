# c7e17_bounce.py
# Tony Chen

from graphics import *

def main():
    print("This program animates a circle bouncing around a window.\n")

    input("Press <Enter> to continue.")

    win = GraphWin("Bounce", 500, 300)
    win.setCoords(-250, -150, 250, 150)

    text = Text(Point(0, 0),
                "Click to indicate the center of the circle.")
    text.draw(win)

    a = win.getMouse()

    circle = Circle(a, 30)
    circle.draw(win)

    text.setText("Please click to indicate the direction of the first move.")

    b = win.getMouse()

    if b.getX() > a.getX():
        dx = 1
    else:
        dx = -1

    if b.getY() > a.getY():
        dy = 1
    else:
        dy = -1
        

    text.undraw()

    d = a

    # for i in range(10000):
    while True:
        circle.move(dx, dy)
        
        c = circle.getCenter()

        Line(c, d).draw(win)
        
        if c.getX() >= 219:
            dx = -1
        elif c.getX() <= -219:
            dx = 1

        if c.getY() >= 119:
            dy = -1
        elif c.getY() <= -119:
            dy = 1

        d = c

        update(100)

    try:
        win.getMouse()
        win.close()
    except:
        pass

if __name__ == "__main__":
    main()
