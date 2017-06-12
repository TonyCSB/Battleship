# c3e17_newton.py
# Tony Chen

import math

def main():
    print("This program uses Newton's method to approximate" + 
                "the square")
    print("root of a number.")
    print()
    x = float(input("What number would you like to know the" +
            "square root of? "))
    n = int(input("How many time should the approximation be" +
            "improved? "))

    guess = x / 2

    for i in range(n):
        guess = (guess + x / guess) / 2

    print("The value calculated by this program is:", guess)

    d = abs(guess - math.sqrt(x))

    print("This value is within", d, "of math.sqrt(x).")

main()
