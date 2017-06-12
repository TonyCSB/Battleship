# c3e12_cubes.py
# Tony Chen

def main():
    print("This program calculates the sum of the cubes of the first natural numbers.")
    n = int(input("Please enter a number: "))
    result = 0

    for i in range (n):
        result = result + i ** 3

    print("The answer is", result)

main()
