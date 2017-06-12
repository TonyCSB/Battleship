# c3e10_ladder.py
# Tony Chen

def main():
    height = float(input("Please enter the height: "))
    angleDegree = float(input("Please enter the angle of the ladder in degrees: "))

    import math

    angleRadian = math.pi / 180 * angleDegree
    length = height / (math.sin(angleRadian))

    print("The length of the ladder should be", length)

main()
