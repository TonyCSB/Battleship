# c3e7_distance.py
# Tony Chen

def main():
    print("This program determines the distance between two")
    print("points, each entered as two numbers separated by")
    print("a comma.")

    print()
    
    x1, y1 = eval(input("Please enter the coordinate of the first point: "))
    x2, y2 = eval(input("Please enter the coordinate of the second point: "))

    import math

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print()

    print("The distance between (", x1,",", y1,") and (", x2,",",y2,") is", distance)

main()
