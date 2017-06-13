# c3e10_ladder.py
# Tony Chen

import math

def main():
    print("This program determines the length of a ladder required")
    print("to reach a given height, when leaned against a wall at a ")
    print("given angle.")

    print()
    
    height = float(input("Please enter the height in feet : "))
    angleDegree = float(input("Please enter the angle of the" +
                              " ladder in degrees: "))

    print()

    angleRadian = math.pi / 180 * angleDegree
    length = height / (math.sin(angleRadian))

    length = round(length, 2)

    print("The length of the ladder should be", length)

main()
