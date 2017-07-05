# c7e5_bmi.py
# Tony Chen

def main():
    print("This program calculates the BMI based on")
    print("input weight and height.\n")

    w = float(input("Weight(in pounds)? "))
    h = float(input("Height(in inches)? "))

    bmi = w * 720 / (h ** 2)

    if bmi > 25:
        print("\nYour BMI is above the healthy range.")
    elif bmi >= 19:
        print("\nYour BMI is within the healthy range.")
    else:
        print("\nYour BMI is below the healthy range.")

main()
