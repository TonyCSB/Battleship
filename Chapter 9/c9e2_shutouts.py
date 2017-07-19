# c9e2_shutouts.py
# Tony Chen

from random import random

def main():
    printIntro()
    probA, probB, n = getInput()
    winsA, winsB, aShutOut, bShutOut = simNGames(n, probA, probB)
    printSummary(winsA, winsB, aShutOut, bShutOut)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each players is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def getInput():
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulates? "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    aShutOut = 0
    bShutOut = 0
    
    for i in range(n):
        scoreA, scoreB, shutOut = simOneGame(probA, probB)
        
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1

        if shutOut == "A":
            aShutOut = aShutOut + 1
        elif shutOut == "B":
            bShutOut = bShutOut + 1
        
    return winsA, winsB, aShutOut, bShutOut

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    isShutOut = False
    
    while not (gameOver(scoreA, scoreB) or shutOut(scoreA, scoreB)):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
                
    if shutOut(scoreA, scoreB):
        if scoreA == 7 and scoreB == 0:
            isShutOut = "A"
        else:
            isShutOut = "B"
    
    return scoreA, scoreB, isShutOut

def gameOver(a, b):
    return a == 15 or b == 15

def shutOut(a, b):
    return (a == 7 and b == 0) or (b == 7 and a == 0)

def printSummary(winsA, winsB, aShutOut, bShutOut):
    n = winsA + winsB

    print("\nGames simulated:", n)
    
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))

    print("Shutouts for A: {0} ({1:0.1%})".format(aShutOut, aShutOut / winsA))
    print("Shutouts for B: {0} ({1:0.1%})".format(bShutOut, bShutOut / winsA))

if __name__ == "__main__":
    main()
