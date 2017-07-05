# maxn.py
# John Zelle

def main():
    n = int(input("How many numbers are there? "))

    maxval = float(input("Enter a number >> "))

    for i in range(n - 1):
        x = float(input("Enter a number >> "))
        if x > maxval:
            maxval = x

    print("The largest value is", maxval)

main()
