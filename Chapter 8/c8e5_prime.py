# c8e5_prime.py
# Tony Chen

from math import sqrt

def main():
    print("This program determines if the input number is a prime.\n")

    n = int(input("Number? "))

    a = n > 1 and all(n % i for i in range(2, int(sqrt(n)) + 1))

    if a:
        print("\nIt is a prime.")
    else:
        print("\nIt is not a prime.")

main()
        
