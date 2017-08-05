# button.py
# Tony Chen

from graphics import *
from time import sleep

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """Creates a rectanglular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit')"""

        self.win = win
        self.center = center
        self.width = width
        self.height = height
        self.label = label

        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)

        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def move(self, x, y):
        self.label.move(x, y)
        self.rect.move(x, y)

    def setFace(self, face):
        "Set the face of the text in the button"
        self.label.setFace(face)

    def setSize(self, size):
        "Set the size of the text in the button"
        self.label.setSize(size)

    def clicked(self, p):
        "Returns true if button active and p is inside."
        result = False
        
        if (self.active and
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax):
                result = True
                self.rect.setFill('grey')
                sleep(0.1)
                self.rect.setFill('darkgrey')

        return result

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setOutline("blue2")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        
