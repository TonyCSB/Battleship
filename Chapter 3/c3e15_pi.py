# c3e15_pi.py
# Tony Chen

import math

def main():
    print("This program approximates the value of pi by summing")
    print("the terms in a series (4/1 + -4/3 + 4/5 + ...).")

    print()
    
    n = int(input("Enter the number of terms to sum: "))
    pi = 0

    for i in range(0, n, 2):
        pi = 4 / (2 * i + 1) - 4 / (2 * (i + 1) + 1) + pi

    print()

    print("The approximation of pi is", pi)

    accuracy = abs(math.pi - pi)

    print("This is within", accuracy, "of math.pi.")

main()
        
