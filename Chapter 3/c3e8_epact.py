# c3e8_epact.py
# Tony Chen

def main():
    print("Given a year, this program calculates the number of")
    print("days between January 1st and the previous new moon,")
    print("also called the 'Gregorian epact.'")
    print()
    
    year = int(input("Please enter the year: "))

    print()

    c = year // 100

    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30

    print("The epact for", year, "is:", epact)

main()
