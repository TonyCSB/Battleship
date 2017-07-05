# c7e12_date_check.py
# Tony Chen

def isLeap(year):
    d4 = year % 4
    d100 = year % 100
    d400 = year % 400

    if d4 == 0:
        if d400 == 0:
             x = 0
        elif d100 == 0:
            x = -1
        else:
            x = 0
    else:
        x = -1

    return x

def is28Days(day):
    if day <= 28:
        return 0
    else:
        return -1

def is29Days(day):
    if day <= 29:
        return 0
    else:
        return -1

def is30Days(day):
    if day <= 30:
        return 0
    else:
        return -1

def is31Days(day):
    if day <= 31:
        return 0
    else:
        return -1

def dateSplit(date):
    month, day, year = date.split("/")
    
    month = int(month)
    day = int(day)
    year = int(year)

    return month, day, year

def main():
    print("This program can determine if the date is valid.\n")

    try:
        date = input("Please enter the date (mm/dd/yyyy): ")

        month, day, year = dateSplit(date)

        if month < 7:
            if month % 2 == 1:
                x = is31Days(day)
            elif month == 2:
                if isLeap(year) == 0:
                    x = is29Days(day)
                else:
                    x = is28Days(day)
            else:
                x = is30Days(day)
        else:
            if month % 2 == 1:
                x = is30Days(day)
            else:
                x = is31Days(day)

        
        if month < 0:
            x = -1

        if month > 12:
            x = -1

        if day < 0:
            x = -1

        if x == 0:
            print("\nThis is a valid date.")
        else:
            print("\nThis is not a valid date.")

    except:
        print("\nThis is not a valid date.")

if __name__ == "__main__":
    main()
