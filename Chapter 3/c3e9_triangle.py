# c3e9_triangle.py
# Tony Chen

def main():
    print("This program calculates the area of a triangle,")
    print("given the length of its three sides entered as")
    print("three numbers separated by a comma.")

    print()
    
    a, b, c = eval(input("Please enter the length of the triangle's three sides: "))

    import math

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print()

    print("The area of the given triangle is", area)

main()
