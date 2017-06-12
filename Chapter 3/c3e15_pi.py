# c3e15_pi.py
# Tony Chen

def main():
    print("This program approximates the value of pi.")
    n = int(input("Enter the number of terms to sum: "))
    pi = 0

    import math

    for i in range(0, n, 2):
        pi = 4 / (2 * i + 1) - 4 / (2 * (i + 1) + 1) + pi

    print("The approximation of pi is", pi)

    accuracy = math.pi - pi

    print("The accuracy is", accuracy)

main()
        
