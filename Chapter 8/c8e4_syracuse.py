# c8e4_syracuse.py
# Tony Chen

def main():
    print("This program generates the Syracuse sequence,")
    print("starting with a natural number (an integer greater")
    print("than or equal to 1).\n")

    n = int(input("Starting value? "))

    print(n, end = "")

    while n != 1:
        if n % 2 == 0:
          n = n / 2

        else:
          n = 3 * n + 1

        print(", {0}".format(int(n)), end = "")

main()
