# c8e11_degree_days.py
# Tony Chen

def main():
    print("This program calculates heating degree-days and")
    print("cooling degree-dats for a year of average daily")
    print("(Fahrenheit) temperature values.\n.")

    n = input("Enter the temperature (Press <Enter> to quit): ")

    cool = 0
    heat = 0

    while n != "":
        x = float(n)
        if x < 60:
            heat = heat + 60 - x
        elif x > 80:
            cool = cool + x - 80
            
        n = input("Enter the temperature (Press <Enter> to quit): ")

    print("\nHeating degree-days:{0:>7.2f}".format(heat))
    print("Cooling degree-days:{0:>7.2f}".format(cool))

main()
