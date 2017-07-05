# c7e13_day_number.py
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

def isValid(dateStr):
    try:
        month, day, year = dateSplit(dateStr)

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
            return 0
        else:
            return -1

    except:
        return -1

def main():
    print("This program calculates the corresponding day number.\n")

    try:
        dateStr = input("Date(mm/dd/yyyy)? ")

        if isValid(dateStr) == 0:
            month, day, year = dateSplit(dateStr)
            dayNum = 31 * (month - 1) + day

            if month > 2:
                dayNum = dayNum - (4 * month + 23) // 10
                if isLeap(year) == 0:
                    dayNum = dayNum + 1

            print("\nThe day number is {0}.".format(dayNum))
        else:
            print("\nThis is not a valid date.")

    except:
        print("\nThis is not a valid date.")

if __name__ == "__main__":
    main()

