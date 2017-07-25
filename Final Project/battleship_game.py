# battleship_game.py
# Tony Chen

from graphics import *
from random import random

def drawWindow():
    global win

    win = GraphWin("Battleship", 500, 500)
    win.setCoords(-2, 11, 11, -2)

def printIntro():
    global win

    intro = Text(Point(4.5, 4.5), "Welcome to the game of Battleship!\n\n" +
                 "Press <Enter> to continue.")
    intro.draw(win)

    win.getKey()
    intro.undraw()

def drawInterface():
    drawNumbers()
    drawLetters()
    drawLines()

def drawNumbers():
    global win

    x = -0.5

    for i in range(1, 11):
        Text(Point(x, i - 0.5), i).draw(win)

def drawLetters():
    global win

    y = -0.5

    for i in range(1, 11):
        Text(Point(i - 0.5, y), chr(64 + i)).draw(win)

def drawLines():
    
    for i in range(-1, 11):
        a = Point(i, -1)
        b = Point(i, 10)
        drawLine(a, b)

        a = Point(-1, i)
        b = Point(10, i)
        drawLine(a, b)

def drawLine(a, b):
    global win
    
    line = Line(a, b)
    line.setFill("Blue Violet")
    line.draw(win)

def randomShips():    
    randomCarrier()
    randomBattleship()
    randomCruiser()
    randomSubmarine()
    randomDestroyer()

def randomCarrier():
    global xList
    global yList

    x, y = randomPoint()

    direction = getDirection(x, y, 5)

    xList = []
    yList = []

    appendList(direction, 5, x, y)

def randomBattleship():

    while True:
        x, y = randomPoint()

        while isHit(x, y):
            x, y = randomPoint()

        direction = getDirection(x, y, 4)

        errors = appendList(direction, 4, x, y)

        if errors == False:
            break
        
        del xList[-4:]
        del yList[-4:]

def randomCruiser():

    while True:
        x, y = randomPoint()

        while isHit(x, y):
            x, y = randomPoint()

        direction = getDirection(x, y, 3)

        errors = appendList(direction, 3, x, y)

        if errors == False:
            break

        del xList[-3:]
        del yList[-3:]

def randomSubmarine():
    randomCruiser()

def randomDestroyer():

    while True:
        x, y = randomPoint()

        while isHit(x, y):
            x, y = randomPoint()

        direction = getDirection(x, y, 2)

        errors = appendList(direction, 2, x, y)

        if errors == False:
            break

        del xList[-2:]
        del yList[-2:]

def getDirection(x, y, n):
    up = True
    down = True
    left = True
    right = True

    if y <= n - 2:
        up = False
        
    elif y >= -n + 11:
        down = False

    if x <= n - 2:
        left = False

    elif x >= -n + 11:
        right = False

    direction = randomDirection()

    while eval(direction) == False:
        direction = randomDirection()

    return direction
        
def appendList(direction, n, x, y):
    global xList
    global yList
    
    errors = False

    if direction == "up":
        for i in range(n):
            if isHit(x, y):
                error = True
                if errors or error:
                    errors = True

            xList.append(x)
            yList.append(y)

            y = y - 1

    elif direction == "down":
        for i in range(n):
            if isHit(x, y):
                error = True
                if errors or error:
                    errors = True

            xList.append(x)
            yList.append(y)

            y = y + 1

    elif direction == "left":
        for i in range(n):
            if isHit(x, y):
                error = True
                if errors or error:
                    errors = True

            xList.append(x)
            yList.append(y)

            x = x - 1

    else:
        for i in range(n):
            if isHit(x, y):
                error = True
                if errors or error:
                    errors = True

            xList.append(x)
            yList.append(y)

            x = x + 1

    return errors

def isHit(x, y):
    global xList
    global yList

    i = 0
    hit = False
    
    while True:
        if xList == []:
            break
        
        if x == xList[i] and y == yList[i]:
            hit = True
            break
        
        i = i + 1

        if i == len(xList):
            break
        
    return hit

def randomPoint():

    x = int(random() * 10)
    y = int(random() * 10)

    return x, y

def randomDirection():

    a = random()

    if a <= 0.25:
        return "up"

    elif a <= 0.5:
        return "down"

    elif a <= 0.75:
        return "left"

    else:
        return "right"

def playGame():
    global win
    global xClickList
    global yClickList

    xClickList = []
    yClickList = []

    hit = 0
    click = 0

    text = Text(Point(4.5, -1.5), "Hit: {0:>3}         Round: {1:>3}"
                .format(hit, click))
    text.draw(win)
    
    while hit != 17:
        x, y = getMouse()

        if isEffect(x, y):

            if isHit(x, y):
                drawSink(x, y)
                hit = hit + 1
                
            else:
                drawMiss(x, y)

            click = click + 1

        text.setText("Hit: {0:>3}         Round: {1:>3}".format(hit, click))

    text.setText("It takes you {0} tries to finish the game.".format(click))

def getMouse():
    global win

    a = win.getMouse()

    x, y = a.getX(), a.getY()

    if x >= 0 and y >= 0:
        x, y = int(x), int(y)

    return x, y

def drawSink(x, y):
    global win
    
    circle = Circle(Point(x + 0.5, y + 0.5), 0.3)
    circle.setOutline("Red")
    circle.setWidth(0.3)
    circle.draw(win)

def drawMiss(x, y):
    global win

    line1 = Line(Point(x + 0.1, y + 0.1), Point(x + 0.9, y + 0.9))
    line1.setOutline("Red")
    line1.setWidth(0.3)
    line1.draw(win)

    line2 = Line(Point(x + 0.1, y + 0.9), Point(x + 0.9, y + 0.1))
    line2.setOutline("Red")
    line2.setWidth(0.3)
    line2.draw(win)

def isEffect(x, y):
    global xClickList
    global yClickList
    
    click = False
    i = 0

    if (x >= 0 and x <= 9) and (y >= 0 and y <= 9):
        click = True
        
        while True:
            if xClickList == []:
                break
            
            if x == xClickList[i] and y == yClickList[i]:
                click = False
                break
            
            i = i + 1

            if i == len(xClickList):
                break

    if click == True:     
        xClickList.append(x)
        yClickList.append(y)
            

    return click

def exitGame():
    global win

    try:
        win.getMouse()
        win.close()
        
    except:
        pass
    
def main():
    try:
        drawWindow()
        printIntro()
        drawInterface()
        randomShips()
        playGame()
        exitGame()

    except:
        pass
    
if __name__ == "__main__":
    main()
