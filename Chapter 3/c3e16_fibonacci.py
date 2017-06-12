# c3e16_fibonacci.py
# Tony Chen

def main():
    print("This program calculates for a certain Fibonacci sequence.")
    n = int(input("Which Fibonacci number to you want to find? "))
    a = 1
    b = 1

    for i in range(n - 2):
        a, b = b, a + b

    print("The Fibonacci number is", b)

main()
