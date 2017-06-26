# c5e11_chaos.py
# Tony Chen

def main():
    numbers = input("Please enter two values between 0 and 1 " +
                    "(separated by space): ")

    n = int(input("Please enter the number of iterations: "))

    print()
    
    x, y = numbers.split()

    x, y = float(x), float(y)

    print("{0}     {1:^5.3}      {2:^5.3}".format("index", x, y))
    print("------------------------------")

    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(" {0:>2}     {1:^8.6f}    {2:^8.6f}".format(i + 1, x, y))

main()
