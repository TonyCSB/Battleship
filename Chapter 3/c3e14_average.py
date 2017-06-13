# c3e14_average.py
# Tony Chen

def main():
    print("This program calculates the average of a series of numbers.")

    print()
    
    n = int(input("How many numbers are you going to enter? "))
    value = 0

    print()

    for i in range(n):
        a = float(input("Please the enter the number: "))
        value = value + a

    average = value / n

    print()

    print("The average of these numbers is", average)

main()
