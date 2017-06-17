# c4e10_triangle.py
# Tony Chen

from graphics import *
import math

def main():
    # Window is wide enough that the instruction text has space on
    # the left and right.
    w = GraphWin("c4e7_circle.py", 600, 400)
    w.setCoords(-15, -10, 15, 10)

    # Notice how you can display more than one line of text...
    # Each line ends with '\n', the 'newline' special character
    # which, instead of being printed, shows up as a line break.
    # And multiple lines are joined into a single string by using
    # plus signs.
    t = Text(Point(0, 0),
        "This program computes the intersection of a\n" +
        "circle and a horizontal line, and then displays\n" +
        "the information in the window.\n" +
        "\n" + # This is to put a blank line after the first
               # sentence.
        "(Click to continue.)")
    t.draw(w)

    w.getMouse()  # Wait for a mouse click.
    t.undraw()    # Erase first set of instructions.

    # Change text of t, so that it will be the second set of
    # instructions.  (Next time t is drawn, it will show up as the
    # second set of instructions instead of the first.)
    t.setText(
        "The center of the circle will be the center of the\n" +
        "window.  Click some distance away from the center to\n" +
        "show how big you'd like the circle to be.  After\n" +
        "that, click somewhere within the vertical range of\n" +
        "the circle to show where you'd like the y-intercept\n" +
        "of the line to be.")
    t.draw(w)

    p = w.getMouse()  # Wait for a mouse click, but this time save
                      # the location of the click in a variable so
                      # we have it later.
    t.undraw()        # Erase second set of instructions.

    # Distance from the center (0, 0) to the place where they
    # clicked will be the radius of the circle.
    r = math.sqrt(p.getX() ** 2 + p.getY() ** 2)

    c = Circle(Point(0, 0), r)
    c.draw(w)

    p = w.getMouse()
    y = p.getY()   # Y-intercept is y value of most recent mouse
                   # click.

    x = math.sqrt((r ** 2) - (y ** 2))  # Formula from the
                                        # instructions in the book
                                        # for exercise 7.

    m = Line(Point(-15, y), Point(15, y))
    m.draw(w)
    p = Circle(Point(-x, y), 0.15)
    p.setFill("red")
    p.draw(w)
    p = p.clone()
    p.move(2 * x, 0)
    p.draw(w)

    # If you want to combine character strings and numbers into a
    # single string (which you need to do if you want to put
    # numbers in a graphics.py Text object), you can use the str
    # function to turn the numerical values into strings, and then
    # plus signs to join those with quoted character strings.
    # (I've also rounded the values so that they won't take up too
    # much space in the window.)
    t.setText("The points of intersection are:\n" +
        "\n" +
        "(" + str(round(-x, 2)) + ", " + str(round(y, 2)) + ")\n" +
        "(" + str(round(x, 2)) + ", " + str(round(y, 2)) + ")")
    t.draw(w)

    # One more click will close the window.
    w.getMouse()
    w.close()

main()
