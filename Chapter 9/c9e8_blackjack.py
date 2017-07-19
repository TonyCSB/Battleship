# c9e8_blackjack.py
# Tony Chen

from random import randrange

def printIntro():
    print("This program simulates the blackjac games. It calculates")
    print("the probability of the dealer busts.\n")

def getInput():
    n = int(input("How many games to simulates? "))
    return n

def simOneGame():
    total, hasAce = getCard()
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
    wins = 0
    
    for i in range(n):
        if simOneGame():
            wins = wins + 1

    loses = n - wins

    return loses

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

def printSummary(loses, n):
    print("\nThe result of the simulations is:")
    print("Busts for dealer: {0} ({1:0.1%})".format(loses, loses / n))

def main():
    printIntro()
    n = getInput()
    loses = simNGames(n)
    printSummary(loses, n)

if __name__ == "__main__":
    main()
