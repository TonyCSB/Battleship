# c8e7_goldbach.py
# Tony Chen

from math import sqrt

def isPrime(n):
    a = n > 1 and all(n % i for i in range(2, int(sqrt(n)) + 1))
    return a

def isEven(n):
    a = n > 2 and n % 2 == 0
    return a

def main():
    print("This program, given an even number greater than 2,")
    print("searches for pairs of prime numbers whose sum is ")
    print("equal to that number.\n")

    n = int(input("Enter an even number: "))

    while isEven(n) == False:
        print("\nPlease enter an even number (greater than 2).\n")
        n = int(input("Enter an even number: "))

    a = 0
    print()

    while a <= n / 2:
        b = n - a
        if isPrime(a) and isPrime(b):
            print("{0:>2.0f} + {1:>2.0f} = {2:>2.0f}".format(a, b, n))

        a = a + 1
main()
