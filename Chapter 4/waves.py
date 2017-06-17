# waves.py
# David Owen

import time # For sleep function.

from graphics import *

def main():

    # Make a window with title "waves.py" and pixel dimensions
    # 320x240.  Make the window background white.
    w = GraphWin("waves.py", 320, 240)
    w.setBackground("white")

    # Wait until we get a mouse click; when we do, assign the
    # click point to p.
    p = w.getMouse()

    # Draw a dark gray circle centered at p, with radius r = 3.
    # (color_rgb makes a color from three numbers in the range
    # 0-255.  The numbers represent the red, green and blue
    # components of the color.  If the numbers are low, the color
    # is dark; if they're high, it's light. Three low numbers,
    # all the same, makes dark gray.)
    r = 3
    c = Circle(p, r)
    c.setOutline(color_rgb(r * 2, r * 2, r * 2))
    c.draw(w)

    time.sleep(0.1) # Pause 1/10 of a second.

    # Draw a little bit lighter and bigger circle...
    r = r + 6
    d = Circle(p, r)
    d.setOutline(color_rgb(r * 2, r * 2, r * 2))
    d.draw(w)
    time.sleep(0.1)

    # Draw a little bit lighter and bigger circle...
    r = r + 6
    e = Circle(p, r)
    e.setOutline(color_rgb(r * 2, r * 2, r * 2))
    e.draw(w)
    time.sleep(0.1)

    # Draw a little bit lighter and bigger circle...
    r = r + 6
    f = Circle(p, r)
    f.setOutline(color_rgb(r * 2, r * 2, r * 2))
    f.draw(w)
    time.sleep(0.1)

    # Each time through the loop, erase the fourth-to-last circle.
    # Then make a new circle, a little bit lighter and bigger than
    # the last one.  Then reassign variable names so that, the
    # next time through the loop, the third-to-last will become
    # the fourth-to-last, the second-to-last the third-to-last, etc.
    for i in range(r + 6, 256 // 2, 6):
        time.sleep(0.1)
    
        c.undraw() # Erase smallest (not yet erased) circle.

        # Replace smallest with a circle bigger than any drawn yet.
        c = Circle(p, i)
        c.setOutline(color_rgb(i * 2, i * 2, i * 2))
        c.draw(w)

        # Update variables so that c is smallest, d is next, e is next,
        # then f.
        c, d, e, f = d, e, f, c

    # Erase the final four circles.
    time.sleep(0.1)
    c.undraw()
    time.sleep(0.1)
    d.undraw()
    time.sleep(0.1)
    e.undraw()
    time.sleep(0.1)
    f.undraw()
    
    # Wait for mouse click, then close window.
    w.getMouse()
    w.close()
       
main()
