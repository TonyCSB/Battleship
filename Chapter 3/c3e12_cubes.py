# c3e12_cubes.py
# Tony Chen

def main():
    print("This program calculates the sum of the cubes of")
    print("the first n natural numbers.")

    print()
    
    n = int(input("Please enter the value of n: "))
    result = 0

    for i in range (n):
        result = result + (i + 1) ** 3

    print()

    print("The answer is", result)

main()
