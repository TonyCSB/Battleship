# c9e5_volleyball.py
# Started by David Owen, completed by Tony Chen.

from random import random

def printIntro():

    print("This program simulates volleyball games between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1).")
    print("This program tries to determine if the rally scoring")
    print("magnifies, reduces or has no effect on the relative")
    print("advantage enjoyed by the better team.\n")

def getInputs():
    
    a = float(input("What is the prob. player A wins? "))
    b = float(input("What is the prob. player B wins? "))
    n = int(input("How many games to simulates? "))
    return a, b, n

def normalGameOver(scoreA, scoreB):

    return (scoreA >= 15 or scoreB >= 15) and abs(scoreA - scoreB) >= 2

def rallyGameOver(scoreA, scoreB):

    return (scoreA >= 25 or scoreB >= 25) and abs(scoreA - scoreB) >= 2

def simOneGame(probA, probB, scoring):
    serving = "A"
    scoreA = 0
    scoreB = 0

    if scoring == "normal":

        while not normalGameOver(scoreA, scoreB):
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

    else:
        
        while not rallyGameOver(scoreA, scoreB):
            if serving == "A":
                if random() < probA:
                    scoreA = scoreA + 1
                else:
                    scoreB = scoreB + 1
                    serving = "B"
            else:
                if random() < probB:
                    scoreB = scoreB + 1
                else:
                    scoreA = scoreA + 1
                    serving = "A"

    return scoreA, scoreB

def simNGames(n, probA, probB, scoring):
    # You do not need to change this function.  (It's copied from
    # the racquetball example on pages 282-284, but modified to
    # account for the possibility of multiple ways of scoring a
    # game.)

    winsA = winsB = 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, scoring)

        if scoreA > scoreB:
            winsA = winsA + 1

        else: # (Tie not possible.)
            winsB = winsB + 1

    return winsA, winsB

def printSummary(winsA, winsB):
    # You do not need to change this function either.  (It's
    # also from the racquetball example on pages 282-284.)

    n = winsA + winsB
    print("  Games simulated:", n)
    print("  Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("  Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))

def main():
    # And you do not need to change this function.  (It's also
    # from the racquetball example on pages 282-284.)

    printIntro()
    probA, probB, n = getInputs()

    print()
    print("Normal Scoring".center(30))
    print("-" * 30)

    winsA, winsB = simNGames(n, probA, probB, "normal")
    printSummary(winsA, winsB)

    print()
    print("Rally Scoring".center(30))
    print("-" * 30)

    winsA, winsB = simNGames(n, probA, probB, "rally")
    printSummary(winsA, winsB)

if __name__ == "__main__":
    main()
