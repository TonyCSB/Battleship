# c7e7_babysitter.py
# Tony Chen

def toDecimalHours(time):
    hour, minute = time.split(":")
    time = int(hour) + int(minute) / 60
    return time

def main():
    print("This program calculates the total bill for a (very cheap!)")
    print("babysitter who charges $2.50 per hour until 9:00 and $1.75")
    print("per hour after 9:00.  (Start and end times are assumed to")
    print("fall between 1:00 PM and 11:59 PM on the same day.)\n")
    
    start = input("Start time (e.g., 7:30)? ")
    end = input("End time? ")

    start = toDecimalHours(start)
    end = toDecimalHours(end)

    if end <= 9:
        time = end - start
        pay = time * 2.5
    elif start >= 9:
        time = end - start
        pay = time * 1.75
    else:
        time1 = 9 - start
        time2 = end - 9
        pay = time1 * 2.5 + time2 * 1.75

    print("\nThe babysitter's pay should be ${0:.02f}.".format(pay))

if __name__ == "__main__":
    main()
