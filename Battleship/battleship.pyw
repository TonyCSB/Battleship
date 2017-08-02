# battleship_game_3.0.py
# Tony Chen

##  Version 3.0
##      - able to identify if the ships are placed on one line

from graphics import *
from random import random

def drawWindow():
    global win

    win = GraphWin("Battleship", 1000, 500)
    win.setCoords(-10, -10, 10, 10)

def printIntro():
    global win

    intro = Text(Point(0, 2), "Welcome to the game of Battleship!")
    intro.setSize(25)
    intro.setFace("helvetica")
    intro.draw(win)

    square1 = Rectangle(Point(1, -1), Point(4, -3))
    square1.draw(win)

    square2 = square1.clone()
    square2.move(-5, 0)
    square2.draw(win)

    text1 = Text(Point(2.5, -2), "Two Players")
    text1.setFace("helvetica")
    text1.setSize(15)
    text1.draw(win)

    text2 = text1.clone()
    text2.move(-5, 0)
    text2.setText("Single Player")
    text2.draw(win)

    while True:
        a = win.getMouse()
        x, y = a.getX(), a.getY()

        if -4 <= x <= -1 and -3 <= y <= -1:
            mode = "single"
            break
        
        elif 1 <= x <= 4 and -3 <= y <= -1:
            mode = "multiple"
            break

    for i in [intro, square1, square2, text1, text2]:
        i.undraw()

    return mode

def drawInterface():
    drawNumbers(-0.5)
    drawLetters(0)
    drawLines(0)

def drawInterfaces():
    global win
    
    drawInterface()
    drawNumbers(12.5)
    drawLetters(13)
    drawLines(13)

def drawNumbers(x):
    global win

    for i in range(1, 11):
        Text(Point(x, i - 0.5), i).draw(win)

def drawLetters(a):
    global win

    y = -0.5

    for i in range(1, 11):
        Text(Point(i - 0.5 + a, y), chr(64 + i)).draw(win)

def drawLines(n):
    
    for i in range(-1, 11):
        a = Point(i + n, -1)
        b = Point(i + n, 10)
        drawLine(a, b)

        a = Point(-1 + n, i)
        b = Point(10 + n, i)
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

        while isHit(x, y, 0):
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

        while isHit(x, y, 0):
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

        while isHit(x, y, 0):
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
            if isHit(x, y, 0):
                error = True
                if errors or error:
                    errors = True

            xList.append(x)
            yList.append(y)

            y = y - 1

    elif direction == "down":
        for i in range(n):
            if isHit(x, y, 0):
                error = True
                if errors or error:
                    errors = True

            xList.append(x)
            yList.append(y)

            y = y + 1

    elif direction == "left":
        for i in range(n):
            if isHit(x, y, 0):
                error = True
                if errors or error:
                    errors = True

            xList.append(x)
            yList.append(y)

            x = x - 1

    else:
        for i in range(n):
            if isHit(x, y, 0):
                error = True
                if errors or error:
                    errors = True

            xList.append(x)
            yList.append(y)

            x = x + 1

    return errors

def isHit(x, y, n):
    global xList, yList
    global xList1, yList1
    global xList2, yList2

    i = 0
    hit = False

    if n == 0:
        while True:
            if xList == []:
                break
            
            if x == xList[i] and y == yList[i]:
                hit = True
                break
            
            i = i + 1

            if i == len(xList):
                break

    elif n == 1:
        while True:
            if xList1 == []:
                break
            
            if x == xList1[i] and y == yList1[i]:
                hit = True
                break
            
            i = i + 1

            if i == len(xList1):
                break

    elif n == 2:
        while True:
            if xList2 == []:
                break
            
            if x == xList2[i] and y == yList2[i]:
                hit = True
                break
            
            i = i + 1

            if i == len(xList2):
                break
        
    return hit

def placeShips():
    global win, xList1, yList1, xList2, yList2

    
    a = Text(Point(4.5, 10.5), "Player 1").draw(win)
    b = Text(Point(17.5, 10.5), "Player 2").draw(win)
    
    xList1, yList1, xList2, yList2 = [], [], [], []
    placeShip("Player1")
    placeShip("Player2")

    a.undraw()
    b.undraw()

def placeShip(player):
    global win, warning1
    
    warning1 = Text(Point(11, -1.5),
                    "Time for " + player + " to place the Carrier.\n" +
                    "(Please click on 5 consecutive grid on the left)")
    warning2 = Text(Point(11, 10.5),
                    "Don't cheat on each other while placing the ships!")

    warning1.draw(win)
    warning2.setTextColor("red")
    warning2.setStyle("bold")
    warning2.draw(win)

    square = Rectangle(Point(10.2, 4), Point(11.8, 5))
    square.draw(win)

    text = Text(Point(11, 4.5), "Done")
    text.draw(win)

    a, b, c, d, e = placeCarrier(player)
    f, g, h, i = placeBattleship(player)
    j, k, l = placeCruiser(player)
    m, n, o = placeSubmarine(player)
    p, q = placeDestroyer()

    while True:
        click = win.getMouse()
        x, y = click.getX(), click.getY()

        if 10.2 <= x <= 11.8 and 4 <= y <= 5:
            break

    shipList = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q]

    for i in shipList:
        i.undraw()

    for i in [warning1, warning2, square, text]:
        i.undraw()

def placeCarrier(text):
    global win, warning1
    global xList1, yList1, xList2, yList2

    carrierListX, carrierListY = [], []

    a = shipCircle(carrierListX, carrierListY)
    b = shipCircle(carrierListX, carrierListY)
    c = shipCircle(carrierListX, carrierListY)
    d = shipCircle(carrierListX, carrierListY)
    e = shipCircle(carrierListX, carrierListY)

    error = False

    if carrierListX[0] == carrierListX[1]:
        for i in range(len(carrierListX) - 1):
            if carrierListX[i] != carrierListX[i + 1]:
                error = True
        carrierListY.sort()
        for i in range(len(carrierListY) - 1):
            if abs(carrierListY[i] - carrierListY[i + 1]) != 1:
                error = True
                
    elif carrierListY[0] == carrierListY[1]:
        for i in range(len(carrierListY) - 1):
            if carrierListY[i] != carrierListY[i + 1]:
                error = True
        carrierListX.sort()
        for i in range(len(carrierListX) - 1):
            if abs(carrierListX[i] - carrierListX[i + 1]) != 1:
                error = True
                
    else:
        error = True

    if error == True:
        for i in [a, b, c, d, e]:
            i.undraw()

        if text[-1] == "1":
            del xList1[-5:]
            del yList1[-5:]
        else:
            del xList2[-5:]
            del yList2[-5:]
        
        warning1.setStyle("bold")
        a, b, c, d, e = placeCarrier(text)
        warning1.setStyle("normal")
        
    warning1.setText("Time for " + text + " to place the Battleship.\n" +
                    "(Please click on 4 consecutive grid)")

    return a, b, c, d, e

def placeBattleship(text):
    global win, warning1
    global xList1, yList1, xList2, yList2

    battleshipListX, battleshipListY = [], []

    a = shipCircle(battleshipListX, battleshipListY)
    b = shipCircle(battleshipListX, battleshipListY)
    c = shipCircle(battleshipListX, battleshipListY)
    d = shipCircle(battleshipListX, battleshipListY)

    error = False

    if battleshipListX[0] == battleshipListX[1]:
        for i in range(len(battleshipListX) - 1):
            if battleshipListX[i] != battleshipListX[i + 1]:
                error = True
        battleshipListY.sort()
        for i in range(len(battleshipListY) - 1):
            if abs(battleshipListY[i] - battleshipListY[i + 1]) != 1:
                error = True
                
    elif battleshipListY[0] == battleshipListY[1]:
        for i in range(len(battleshipListY) - 1):
            if battleshipListY[i] != battleshipListY[i + 1]:
                error = True
        battleshipListX.sort()
        for i in range(len(battleshipListX) - 1):
            if abs(battleshipListX[i] - battleshipListX[i + 1]) != 1:
                error = True
                
    else:
        error = True

    if error == True:
        for i in [a, b, c, d]:
            i.undraw()

        if text[-1] == "1":
            del xList1[-4:]
            del yList1[-4:]
        else:
            del xList2[-4:]
            del yList2[-4:]
        
        warning1.setStyle("bold")
        a, b, c, d = placeBattleship(text)
        warning1.setStyle("normal")

    warning1.setText("Time for " + text + " to place the Cruiser.\n" +
                    "(Please click on 3 consecutive grid)")

    return a, b, c, d

def placeCruiser(text):
    global win, warning1
    global xList1, yList1, xList2, yList2

    cruiserListX, cruiserListY = [], []

    a = shipCircle(cruiserListX, cruiserListY)
    b = shipCircle(cruiserListX, cruiserListY)
    c = shipCircle(cruiserListX, cruiserListY)

    error = False

    if cruiserListX[0] == cruiserListX[1]:
        for i in range(len(cruiserListX) - 1):
            if cruiserListX[i] != cruiserListX[i + 1]:
                error = True
        cruiserListY.sort()
        for i in range(len(cruiserListY) - 1):
            if abs(cruiserListY[i] - cruiserListY[i + 1]) != 1:
                error = True
                
    elif cruiserListY[0] == cruiserListY[1]:
        for i in range(len(cruiserListY) - 1):
            if cruiserListY[i] != cruiserListY[i + 1]:
                error = True
        cruiserListX.sort()
        for i in range(len(cruiserListX) - 1):
            if abs(cruiserListX[i] - cruiserListX[i + 1]) != 1:
                error = True
                
    else:
        error = True

    if error == True:
        for i in [a, b, c]:
            i.undraw()

        if text[-1] == "1":
            del xList1[-3:]
            del yList1[-3:]
        else:
            del xList2[-3:]
            del yList2[-3:]
        
        warning1.setStyle("bold")
        a, b, c = placeCruiser(text)
        warning1.setStyle("normal")

    warning1.setText("Time for " + text + " to place the Submarine.\n" +
                    "(Please click on 3 consecutive grid)")

    return a, b, c

def placeSubmarine(text):
    global win, warning1
    global xList1, yList1, xList2, yList2

    submarineListX, submarineListY = [], []

    a = shipCircle(submarineListX, submarineListY)
    b = shipCircle(submarineListX, submarineListY)
    c = shipCircle(submarineListX, submarineListY)

    error = False

    if submarineListX[0] == submarineListX[1]:
        for i in range(len(submarineListX) - 1):
            if submarineListX[i] != submarineListX[i + 1]:
                error = True
        submarineListY.sort()
        for i in range(len(submarineListY) - 1):
            if abs(submarineListY[i] - submarineListY[i + 1]) != 1:
                error = True
                
    elif submarineListY[0] == submarineListY[1]:
        for i in range(len(submarineListY) - 1):
            if submarineListY[i] != submarineListY[i + 1]:
                error = True
        submarineListX.sort()
        for i in range(len(submarineListX) - 1):
            if abs(submarineListX[i] - submarineListX[i + 1]) != 1:
                error = True
                
    else:
        error = True

    if error == True:
        for i in [a, b, c]:
            i.undraw()

        if text[-1] == "1":
            del xList1[-3:]
            del yList1[-3:]
        else:
            del xList2[-3:]
            del yList2[-3:]
        
        warning1.setStyle("bold")
        a, b, c = placeSubmarine(text)
        warning1.setStyle("normal")

    warning1.setText("Time for " + text + " to place the Destroyer.\n" +
                    "(Please click on 2 consecutive grid)")

    return a, b, c
                     
def placeDestroyer():
    global win, warning1
    global xList1, yList1, xList2, yList2

    destroyerListX, destroyerListY = [], []

    a = shipCircle(destroyerListX, destroyerListY)
    b = shipCircle(destroyerListX, destroyerListY)

    error = False

    if destroyerListX[0] == destroyerListX[1]:
        for i in range(len(destroyerListX) - 1):
            if destroyerListX[i] != destroyerListX[i + 1]:
                error = True
        destroyerListY.sort()
        for i in range(len(destroyerListY) - 1):
            if abs(destroyerListY[i] - destroyerListY[i + 1]) != 1:
                error = True
                
    elif destroyerListY[0] == destroyerListY[1]:
        for i in range(len(destroyerListY) - 1):
            if destroyerListY[i] != detroyerListY[i + 1]:
                error = True
        destroyerListX.sort()
        for i in range(len(destroyerListX) - 1):
            if abs(destroyerListX[i] - destroyerListX[i + 1]) != 1:
                error = True
                
    else:
        error = True

    if error == True:
        for i in [a, b]:
            i.undraw()

        if text[-1] == "1":
            del xList1[-2:]
            del yList1[-2:]
        else:
            del xList2[-2:]
            del yList2[-2:]
        
        warning1.setStyle("bold")
        a, b = placeDestroyer(text)
        warning1.setStyle("normal")

    warning1.setText('You are all set.\nClick on "Done" to clear the marks.')

    return a, b                  

def shipCircle(shipListX, shipListY):
    while True:
        x, y = getMouse(0)

        if isEffect_2(x, y) == True:
            break

    a = drawSunk(x, y)
    
    shipListX.append(x)
    shipListY.append(y)

    return a

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
        x, y = getMouse(0)

        if isEffect_1(x, y, 0):

            if isHit(x, y, 0):
                drawSunk(x, y)
                hit = hit + 1
                isSunk(x, y, 0)
                
            else:
                drawMiss(x, y)

            click = click + 1

        text.setText("Hit: {0:>3}         Round: {1:>3}".format(hit, click))

    text.setText("It takes you {0} tries to finish the game.".format(click))

def playGame2():
    global win, xClickList1, yClickList1, xClickList2, yClickList2
    global hitList1, hitList2, sunkText1, sunkText2

    xClickList1, xClickList2 = [], []
    yClickList1, yClickList2 = [], []
    hitList1, hitList2 = [], []

    sunkText1 = Text(Point(4.5, 10.5), "Player2's turn")
    sunkText1.draw(win)

    sunkText2 = sunkText1.clone()
    sunkText2.move(13, 0)
    sunkText2.setText("")
    sunkText2.draw(win)

    hit1, hit2 = 0, 0
    click1, click2 = 0, 0

    text1 = Text(Point(4.5, -1.5), "Hit: {0:>3}         Round: {1:>3}"
                .format(hit1, click1))
    text1.draw(win)

    text2 = text1.clone()
    text2.move(13, 0)
    text2.draw(win)

    while hit2 != 17:
        while True:
            x, y = getMouse(1)

            if isEffect_1(x, y, 1):
                break
            
        sunkText1.setText("")
        
        if isHit(x, y, 1):
            drawSunk(x, y)
            hit1 = hit1 + 1
            isSunk(x, y, 1)

        else:
            drawMiss(x, y)

        click1 = click1 + 1

        text1.setText("Hit: {0:>3}         Round: {1:>3}".format(hit1, click1))
        sunkText2.setText("Player1's turn")
        
        if hit1 == 17:
            break

        while True:
            x, y = getMouse(2)

            if isEffect_1(x, y, 2):
                break

        sunkText2.setText("")

        if isHit(x, y, 2):
            drawSunk(x, y)
            hit2 = hit2 + 1
            isSunk(x, y, 2)

        else:
            drawMiss(x, y)

        click2 = click2 + 1

        text2.setText("Hit: {0:>3}         Round: {1:>3}".format(hit2, click2))
        sunkText1.setText("Player2's turn")

    for i in [text1, text2, sunkText1, sunkText2]:
        i.undraw()

    if hit1 == 17:
        Text(Point(11, -1.5), "Congratulations, player1 has won the game!").draw(win)
    else:
        Text(Point(11, -1.5), "Congratulations, player2 has won the game!").draw(win)
    
    
def getMouse(n):
    global win

    a = win.getMouse()

    x, y = a.getX(), a.getY()

    if n == 1:
        if 0 <= x <= 10 and y >= 0:
            x, y = int(x), int(y)

    elif n == 2:
        if x >= 13 and y >= 0:
            x, y = int(x), int(y)

    elif n == 0:
        if (0 <= x <= 10 or x >= 13) and y >= 0:
            x, y = int(x), int(y)

    return x, y

def drawSunk(x, y):
    global win
    
    circle = Circle(Point(x + 0.5, y + 0.5), 0.3)
    circle.setOutline("Red")
    circle.setWidth(0.3)
    circle.draw(win)

    return circle

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

def isEffect_1(x, y, n):
    global xClickList, yClickList
    global xClickList1, xClickList2
    global yClickList1, yClickList2
    
    click = False
    i = 0

    if n == 1:
        if (x >= 0 and x <= 9) and (y >= 0 and y <= 9):
            click = True
        
        while True:
            if xClickList1 == []:
                break
            
            if x == xClickList1[i] and y == yClickList1[i]:
                click = False
                break
            
            i = i + 1

            if i == len(xClickList1):
                break

        if click == True:     
            xClickList1.append(x)
            yClickList1.append(y)

    elif n == 2:
        if (x >= 13 and x <= 22) and (y >= 0 and y <= 9):
            click = True
        
        while True:
            if xClickList2 == []:
                break
            
            if x == xClickList2[i] and y == yClickList2[i]:
                click = False
                break
            
            i = i + 1

            if i == len(xClickList2):
                break

        if click == True:     
            xClickList2.append(x)
            yClickList2.append(y)
            
    elif n == 0:
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

def isEffect_2(x, y):
    global xList1, yList1, xList2, yList2
    
    click = False
    i = 0

    if (x >= 0 and x <= 9) and (y >= 0 and y <= 9):
        click = True

        while True:
            if xList1 == []:
                break

            if x == xList1[i] and y == yList1[i]:
                click = False
                break

            i = i + 1

            if i == len(xList1):
                break

        if click == True:
            xList1.append(x)
            yList1.append(y)

    elif (x >= 13 and x <= 22) and (y >= 0 and y <= 9):
        click = True

        while True:
            if xList2 == []:
                break

            if x == xList2[i] and y == yList2[i]:
                click = False
                break

            i = i + 1

            if i == len(xList2):
                break

        if click == True:
            xList2.append(x)
            yList2.append(y)

    return click

def isSunk(x, y, n):
    global hitList, win, xList, yList, sunkText
    global hitList1, hitList2, xList1, xList2
    global yList1, yList2, sunkText1, sunkText2

    i = 0

    if n == 1:
        while True:
            if x == xList1[i] and y == yList1[i]:
                break

            i = i + 1

        if i <= 4:
            hitList1.append(5)
        elif i <= 8:
            hitList1.append(4)
        elif i <= 11:
            hitList1.append(3)
        elif i <= 14:
            hitList1.append(2)
        else:
            hitList1.append(1)

        if hitList1.count(5) == 5:
            sunkText1.setText("You've sunk the enemy carrier!")
            hitList1.remove(5)
            
        elif hitList1.count(4) == 4:
            sunkText1.setText("You've sunk the enemy battleship!")
            hitList1.remove(4)
            
        elif hitList1.count(3) == 3:
            sunkText1.setText("You've sunk the enemy cruiser!")
            hitList1.remove(3)
            
        elif hitList1.count(2) == 3:
            sunkText1.setText("You've sunk the enemy submarine!")
            hitList1.remove(2)
            
        elif hitList1.count(1) == 2:
            sunkText1.setText("You've sunk the enemy destroyer!")
            hitList1.remove(1)

    elif n == 2:
        while True:
            if x == xList2[i] and y == yList2[i]:
                break

            i = i + 1

        if i <= 4:
            hitList2.append(5)
        elif i <= 8:
            hitList2.append(4)
        elif i <= 11:
            hitList2.append(3)
        elif i <= 14:
            hitList2.append(2)
        else:
            hitList2.append(1)

        if hitList2.count(5) == 5:
            sunkText2.setText("You've sunk the enemy carrier!")
            hitList2.remove(5)
            
        elif hitList2.count(4) == 4:
            sunkText2.setText("You've sunk the enemy battleship!")
            hitList2.remove(4)
            
        elif hitList2.count(3) == 3:
            sunkText2.setText("You've sunk the enemy cruiser!")
            hitList2.remove(3)
            
        elif hitList2.count(2) == 3:
            sunkText2.setText("You've sunk the enemy submarine!")
            hitList2.remove(2)
            
        elif hitList2.count(1) == 2:
            sunkText2.setText("You've sunk the enemy destroyer!")
            hitList2.remove(1)
    
    elif n == 0:
    
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
    global win
    
    try:
        drawWindow()
        mode = printIntro()

        if mode == "single":          
            win.setCoords(-8.5, 11, 17.5, -2)
            drawInterface()
            randomShips()
            playGame()
            exitGame()

        else:
            win.setCoords(-2, 11, 24, -2)
            drawInterfaces()
            placeShips()
            playGame2()
            exitGame()

    except:
        pass
    
if __name__ == "__main__":
    main()
