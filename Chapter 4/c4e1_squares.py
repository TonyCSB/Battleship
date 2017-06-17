# c4e1_squares.py
# Tony Chen

from graphics import *

def main():
    win = GraphWin()
    
    shape = Rectangle(Point(30, 30), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        
        shape1 = Rectangle.clone(shape)
        shape1.move(dx, dy)
        shape1.draw(win)

    Text(Point(100, 20), "Click again to quit").draw(win)

    win.getMouse()
    win.close()
    
main()
