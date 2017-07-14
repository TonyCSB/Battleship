# event_loop.py
# John Zelle

from graphics import *

def handleKey(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")

def handleClick(pt, win):
    entry = Entry(pt, 10)
    entry.draw(win)

    while True:
        key = win.getKey()
        if key == "Return": break

    entry.undraw()
    typed = entry.getText()
    Text(pt,typed).draw(win)

    win.checkMouse()

def main():
    win = GraphWin("Click and Type", 500, 500)

    while True:
        key = win.checkKey()
        if key == "q":
            break

        if key:
            handleKey(key, win)

        pt = win.checkMouse()

        if pt:
            handleClick(pt, win)

    win.close()

main()
