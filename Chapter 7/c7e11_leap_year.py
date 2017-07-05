# c7e11_leap_year.py
# Tony Chen

def main():
    print("This year calculates if a year is a leap year.\n")

    year = int(input("Year? "))

    d4 = year % 4
    d100 = year % 100
    d400 = year % 400

    if d4 == 0:
        if d400 == 0:
             x = "is"
        elif d100 == 0:
            x = "is not"
        else:
            x = "is"
    else:
        x = "is not"

    print("\n{0} {1} a leap year.".format(year, x))

if __name__ == "__main__":
    main()
