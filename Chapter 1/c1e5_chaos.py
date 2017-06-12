# c1e5_chaos.py
# Tony Chen

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print?"))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

main()
