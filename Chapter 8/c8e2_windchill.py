# c8e2_windchill.py
# Tony Chen

def calc(t, v):
    a = 35.75 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
    return a

def printHead():
    print("╔══", end = "")
    print("╦══" * 11, end = "")
    print("╗")

    print("║    ", end = "")
    for i in range (0, 55, 5):
        print("║{0:^4.0f}".format(i), end = "")
    print("║")

    print("╠══", end = "")
    print("╬══" * 11, end = "")
    print("╣")

def main():
    print("This program generates a table of windchill values, with rows representing")
    print("wind speed (miles per hour) and columns representing temperature (degrees")
    print("Fahrenheit).\n")

    printHead()

    t = -20

    while t != 70:
        print("║{0:^4.0f}║".format(t), end = "")
        for v in range(0, 55, 5):
            print("{0:^4.0f}║".format(calc(t, v)), end = "")

        if t == 60:
            print("\n╚══╩══╩══╩══╩══╩══╩══╩" +
                  "══╩══╩══╩══╩══╝")
        else:
            print("\n╠══╬══╬══╬══╬══╬══╬══╬══╬" +
              "══╬══╬══╬══╣")

        t = t + 10
        
main()
