# c8e6_primes.py
# Tony Chen

from math import sqrt

def isPrime(n):
    a = n > 1 and all(n % i for i in range(2, int(sqrt(n)) + 1))
    return a
    

def main():
    print("This program determines if the input number is a prime.\n")

    n = int(input("Number? "))

    x = 2

    while x != n:
        a = isPrime(x)

        if a:
            print(x)

        x = x + 1
        

main()
        
