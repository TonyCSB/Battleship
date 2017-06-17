# c4e6_futval.py
# Tony Chen

from graphics import *

def main():
    win = GraphWin("Investment Growth Chart", 320, 300)
    win.setBackground("white")
    win.setCoords(-1.75, -2850, 11.5, 10400)
    
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    principal = Entry(Point(6.625, -500), 8)
    principal.draw(win)
    
    apr = Entry(Point(6.625, -1500), 4)
    apr.draw(win)

    win.getMouse()

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()
