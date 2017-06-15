# c4e5_dice.py
# Tony Chen

from graphics import *
from math import *

def main():
    win = GraphWin("Three Dice", 500, 500)
    win.setCoords(0, 0, 7, 7)

    Text(Point(3.5, 6),
         "This program draws three dice in a straight flush.").draw(win)

    length = 1
    lengthSide1 = length * cos(1 / 6 * pi) / 2
    lengthSide2 = length * sin(1 / 6 * pi) / 2

    cube1 = Polygon(Point(1, 3), Point(1, 4), Point(2, 4), Point(2, 3),
                    Point(2 + lengthSide1, 3 + lengthSide2),
                    Point(2 + lengthSide1, 4 + lengthSide2),
                    Point(1 + lengthSide1, 4 + lengthSide2),
                    Point(1, 4), Point(2, 4),
                    Point(2 + lengthSide1, 4 + lengthSide2),
                    Point(2, 4), Point(2, 3))
    cube1.draw(win)

    cube2 = Polygon.clone(cube1)
    cube2.move(2, 0)
    cube2.draw(win)

    cube3 = Polygon.clone(cube2)
    cube3.move(2, 0)
    cube3.draw(win)

    number2_1 = Circle(Point(1.2, 3.2), 0.1)
    number2_1.setFill("Black")
    number2_1.draw(win)

    number2_2 = Circle(Point(1.8, 3.8), 0.1)
    number2_2.setFill("Black")
    number2_2.draw(win)

    number3_1 = Circle.clone(number2_1)
    number3_1.move(2, 0)
    number3_1.draw(win)

    number3_2 = Circle(Point(3.5, 3.5), 0.1)
    number3_2.setFill("Black")
    number3_2.draw(win)

    number3_3 = Circle.clone(number2_2)
    number3_3.move(2, 0)
    number3_3.draw(win)

    number4_1 = Circle.clone(number3_1)
    number4_1.move(2, 0)
    number4_1.draw(win)

    number4_2 = Circle.clone(number4_1)
    number4_2.move(0, 0.6)
    number4_2.draw(win)

    number4_3 = Circle.clone(number3_3)
    number4_3.move(2, 0)
    number4_3.draw(win)

    number4_4 = Circle.clone(number4_3)
    number4_4.move(0, -0.6)
    number4_4.draw(win)

    win.getMouse()
    win.close()
    
main()
