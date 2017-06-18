# c4e6_futval.py
# Tony Chen

from graphics import *

def main():
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")

    win.setCoords(-10, -10, 10, 10)

    text = Text(Point(0, 0),"This program plots the growth\n"+
         "of a 10-year investment.\n"+
         "\n"+
         "(Click to continue)")
    text.draw(win)
    
    win.getMouse()
    text.undraw()

    text = Text(Point(0, 0),"Please enter the initial principal\n"+
                "\n" + "(Click to continue)")
    text.draw(win)
    principal = Entry(Point(0, -5), 8)
    principal.draw(win)

    win.getMouse()

    principal.undraw()
    text.undraw()

    principal = float(principal.getText())
    principal = round(principal, 2)

    text = Text(Point(0, 0),"Please enter the annualized interest rate\n"+
                "\n" + "(Click to continue)")
    text.draw(win)
    apr = Entry(Point(0, -5), 5)
    apr.draw(win)

    win.getMouse()

    apr.undraw()
    text.undraw()

    apr = float(apr.getText())
    
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()

