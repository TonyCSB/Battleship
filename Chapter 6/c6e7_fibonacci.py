# c6e7_fibonacci.py
# Tony Chen

def fibonacci(n):
    a = 1
    b = 1

    for i in range(n - 2):
        a, b = b, a + b

    return b

def main():
    print("This program prints the nth number in the Fibonacci")
    print("series (1, 1, 2, 3, 5, 8, 13...).\n")

    n = int(input("Which Fibonacci number do you want to find? "))

    answer = fibonacci(n)

    print()

    print("The Fibonacci number {0} is {1}.".format(n, answer))

main()
