# c2e6_futval.py
# Tony Chen

def main():
    print("This program calculates the future value")
    print("of a certain year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the number of years: "))

    for i in range (year):
        principal = principal * (1 + apr)

    print("The value in", year, "years is:", principal)

main()
