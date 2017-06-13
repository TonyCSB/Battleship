# c3e16_fibonacci.py
# Tony Chen

def main():
    print("This program prints the nth number in the Fibonacci")
    print("series (1, 1, 2, 3, 5, 8, 13...).")

    print()
    
    n = int(input("Which Fibonacci number to you want to find? "))
    a = 1
    b = 1

    for i in range(n - 2):
        a, b = b, a + b

    print()

    print("The Fibonacci number", n, "is:", b)

main()
