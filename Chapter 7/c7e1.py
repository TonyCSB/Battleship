# c7e1
# Tony Chen

def main():
    print("This program calculates the total wages for the week")
    print("based on the number of hours worked and the hourly rate.\n")
    
    try:
        hour = int(input("Hours? "))
        rate = float(input("Hourly rate? "))

        if 0 <= hour <= 40:
            wage = hour * rate
        elif hour > 40:
            wage = 40 * rate + (hour - 40) * rate * 1.5
        else:
            print("\nPlease enter a positive value!")

        print("\nThe total wages for the week is ${0:0.2f}".format(wage))

    except KeyboardInterrupt:
        print("\nPlease enter a normal value.")

    except:
        pass

main()
