# c6e5_pizza.py
# Tony Chen

from math import *

def pizzaArea(diameter):
    r = diameter / 2
    area = pi * r ** 2
    return area

def pizzaCost(price, diameter):
    cost = price / pizzaArea(diameter)
    return cost

def main():
    print("This program calculates the cost per square inch of")
    print("a circular pizza, given its diameter and price.\n")

    d = float(input("Diameter (in inches)? "))
    p = float(input("Price? "))

    print()

    perCost = pizzaCost(p, d)

    print("The pizza costs ${0:0.2f} per square inch.".format(perCost))

main()
