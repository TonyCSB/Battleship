# c9e9_bust_probabilities.py
# Tony Chen

from random import randrange

def printIntro():
    print("This program simulates the blackjac games. It calculates")
    print("the probability of the dealer busts for each different card.\n")

def getInput():
    n = int(input("How many games to simulates? "))
    return n

def simOneGame(a):
    total = a
    if a == 1:
        hasAce = True
    else:
        hasAce = False
    result = False

    while not burst(total):
        n, Ace = getCard()
        if hasAce or Ace:
            hasAce = True
            
        total = total + n

        if total >= 7 and total <= 11 and hasAce:
            total = total + 10
            result = True
            break
        elif total >= 17 and not burst(total):
            result = True
            break

    return result
        
def simNGames(n):
    losesList = []
    loses = 0
    
    for a in range(1, 11):
        for i in range(n):
            if not simOneGame(a):
                loses = loses + 1
        losesList.append(loses)
        loses = 0

    return losesList

def burst(total):
    return total > 21

def getCard():
    hasAce = False
    
    n = randrange(1, 14)
    if n == 1:
        hasAce = True
    elif n > 10:
        n = 10

    return n, hasAce

def printSummary(losesList, n):
    print("\nThe result of the simulations is:")
    for i in range(1, 11):
        if i == 1:
            a = "ace"
        else:
            a = i
            
        print("Busts for dealer when starts with {0}: {1} ({2:0.1%})".
              format(a, losesList[i - 1], losesList[i - 1] / n))

def main():
    printIntro()
    n = getInput()
    losesList = simNGames(n)
    printSummary(losesList, n)

if __name__ == "__main__":
    main()

