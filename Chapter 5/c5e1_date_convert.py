# c5e1_date_convert.py
# Tony Chen

def main():
    dateStr = input("Please enter a date (mm/dd/yyyy): ")

    monthStr, dayStr, yearStr = dateStr.split("/")

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    monthStr = months[int(monthStr)-1]

    print("The converted date is: {0} {1}, {2}"
          .format(monthStr, dayStr, yearStr))

main()
