# c2e7_futval.py
# Tony Chen

def main():
    print("This program calculates the future value")
    print("of a certain year investment of a fixed amount.")

    investEachYear = eval(input("Enter the the amount to invest each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the number of years: "))
    principal = 0

    for i in range (year):
        principal = (principal + investEachYear) * (1 + apr)

    print("The value in", year, "years is:", principal)

main()
