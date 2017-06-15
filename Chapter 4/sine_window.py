# sine_window.py
# David Owen

import math

from graphics import *  # Requires Zelle's graphics.py in same
                        # directory as this program.

def main():
    # Create a 1000x500 window with title "sine_window.py."
    w = GraphWin("sine_window.py", 1000, 500)

    # Make window background white instead of default light gray.
    w.setBackground("white")

    # Make the lower left corner of the window (-5, -2.5) and the
    # upper right corner of the window (5, 2.5).
    w.setCoords(-5, -2.5, 5, 2.5)

    # Leftmost x value = -5.
    x = -5

    # The window is 1000 pixels wide on the screen, but 10 units
    # wide in the program (because of the call to setCoords above).
    # So the change in x, from one pixel to the next, is 10 / 1000.
    dx = 10 / 1000

    # Loop through the horizontal pixel range of the window.
    for i in range(1000):

        # Math library sine function.
        y = math.sin(x)

        # Draw black point based on value from math library
        # sine function.
        p = Point(x, y)
        p.setFill("black")
        p.draw(w)

        # Taylor series approximation for sine function.
        # (y = x - x^3/3! + x^5/5! - x^7/7! + x^9/9!...)        
        y = x
        y = y - x**3 / math.factorial(3)
        y = y + x**5 / math.factorial(5)
        y = y - x**7 / math.factorial(7)
        # y = y + x**9 / math.factorial(9)

        # Draw blue point based on value from Taylor series
        # approximation of sine function.
        p = Point(x, y)
        p.setFill("blue")
        p.draw(w)

        # Get x value ready for next iteration of the loop.
        x = x + dx
        
    # Wait for mouse click, then close window.
    w.getMouse()
    w.close()

main()
