# thermometer.py
# Tony Chen

from graphics import *

def main():
    win = GraphWin("Thermometer", 100, 300)
    win.setCoords(-4, -40, 4, 140)

    for f in range (-20, 130, 10):
        Point(-1, f).draw(win)
        Line(Point(-1, f),(Point(0, f)), str(f)).draw(win)
        # c = 5 / 9 * f + 32
        # Point(1, f).draw(win)
        # c = int(c)
        # Text(Point(3, f), str(c)).draw(win)

    for c in range (-30, 55, 5):
        f = (9 / 5) * c + 32
        Line(Point(0, f), Point(1, f)).draw(win)
        Text(Point(3, f), str(c)).draw(win)
        

main()
