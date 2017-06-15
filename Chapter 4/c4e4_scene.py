# c4e4_scene.py
# Tony Chen

from graphics import *
from math import *

def main():
    win = GraphWin("A Scene in Summer", 500, 300)
    win.setCoords(0, 0, 10, 6)

    sun = Circle(Point(0, 6), 1.5)
    sun.setWidth(0)
    sun.setFill("Dark Orange")
    sun.draw(win)

    for i in range(9):
        i = i * 10          # Get the degree
        i = i / 180 * pi    # Convert into radians
        
        start1 = 1.7 * sin(i)
        start2 = 6 - 1.7 * cos(i)
        start = Point(start1, start2)

        end1 = 2.3 * sin(i)
        end2 = 6 - 2.3 * cos(i)
        end = Point(end1, end2)

        line = Line(start, end)
        line.setFill("Dark Orange")
        line.draw(win)

    grass = Rectangle(Point(0, 0), Point(10, 1))
    grass.setWidth(0)
    grass.setFill("Chartreuse")
    grass.draw(win)

    house = Rectangle(Point(2, 0), Point(4.25, 2.5))
    house.setFill("Peru")
    house.draw(win)

    for i in range(13):
        i = i / 5
        Line(Point(2, i), Point(4.25, i)).draw(win)

    roof = Polygon(Point(1.5, 2.5), Point(4.75, 2.5), Point(3.125, 3.5))
    roof.setFill("Brown")
    roof.draw(win)

    door = Rectangle(Point(2.25, 0), Point(2.95, 1.25))
    door.setFill("Firebrick")
    door.draw(win)

    doorKnob = Circle(Point(2.4, 0.6), 0.05)
    doorKnob.setFill("Black")
    doorKnob.draw(win)

    window = Rectangle(Point(3.25, 1.5), Point(3.95, 2.2))
    window.setFill("Light Blue")
    window.draw(win)

    windowLine1 = Line(Point(3.25, 1.85), Point(3.95, 1.85))
    windowLine1.draw(win)

    windowLine2 = Line(Point(3.6, 1.5), Point(3.6, 2.2))
    windowLine2.draw(win)

    trunk = Rectangle(Point(7, 0.5), Point(8, 2.75))
    trunk.setFill("Brown")
    trunk.setWidth(0)
    trunk.draw(win)

    tree = Oval(Point(6, 2.25), Point(9, 4.5))
    tree.setFill("Green Yellow")
    tree.setWidth(0)
    tree.draw(win)

    win.getMouse()
    win.close()
    
main()
