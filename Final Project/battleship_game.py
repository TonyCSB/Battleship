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

    intro = Text(Point(4.5, 4), "Welcome to the game of Battleship!")
    intro.draw(win)

    square = Rectangle(Point(3, 5.25), Point(6, 6.75))
    square.draw(win)

    text = Text(Point(4.5, 6), "Continue")
    text.draw(win)
    
    while True:
        a = win.getMouse()

        x, y = a.getX(), a.getY()

        if 3 <= x <= 6 and 5.25 <= y <= 6.75:
            break
        
    intro.undraw()
    square.undraw()
    text.undraw()

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
    global xList, yList

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
    global xList, yList
    
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
    global xList, yList

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
    global win, xClickList, yClickList, hitList, sunkText

    xClickList = []
    yClickList = []
    hitList = []

    hit = 0
    click = 0

    
    sunkText = Text(Point(4.5, 10.5),"")
    sunkText.draw(win)

    text = Text(Point(4.5, -1.5), "Hit: {0:>3}         Round: {1:>3}"
                .format(hit, click))
    text.draw(win)
    
    while hit != 17:
        x, y = getMouse()

        if isEffect(x, y):

            if isHit(x, y):
                drawSunk(x, y)
                hit = hit + 1
                isSunk(x, y)
                
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

def drawSunk(x, y):
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

def isSunk(x, y):
    global hitList, win, xList, yList, sunkText

    i = 0

    while True:
        if x == xList[i] and y == yList[i]:
            break

        i = i + 1

    if i <= 4:
        hitList.append(5)
    elif i <= 8:
        hitList.append(4)
    elif i <= 11:
        hitList.append(3)
    elif i <= 14:
        hitList.append(2)
    else:
        hitList.append(1)

    if hitList.count(5) == 5:
        sunkText.setText("You've sunk the enemy carrier!")
        hitList.remove(5)
        
    elif hitList.count(4) == 4:
        sunkText.setText("You've sunk the enemy battleship!")
        hitList.remove(4)
        
    elif hitList.count(3) == 3:
        sunkText.setText("You've sunk the enemy cruiser!")
        hitList.remove(3)
        
    elif hitList.count(2) == 3:
        sunkText.setText("You've sunk the enemy submarine!")
        hitList.remove(2)
        
    elif hitList.count(1) == 2:
        sunkText.setText("You've sunk the enemy destroyer!")
        hitList.remove(1)    

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
