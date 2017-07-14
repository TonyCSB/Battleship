# c8e2_windchill.py
# Tony Chen

def calc(t, v):
    a = 35.75 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
    return a

def main():
    print("This program generates a table of windchill values, with rows representing")
    print("wind speed (miles per hour) and columns representing temperature (degrees")
    print("Fahrenheit).\n")
    
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦" +
          "══╦══╦══╗\n" +
          "║    ║  0 ║  5 ║ 10 ║ 15 ║ 20 ║ 25 ║ 30 ║ 35 ║" +
          " 40 ║ 45 ║ 50 ║\n" +
          "╠══╬══╬══╬══╬══╬══╬══╬══╬══╬" +
          "══╬══╬══╣")
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
