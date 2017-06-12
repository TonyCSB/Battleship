# c3e8_epact.py
# Tony Chen

def main():
    year = int(input("Please enter the year: "))

    c = year // 100

    epact = (8 + (c // 4) - c + ((8 * c + 13) // 25) + 11 * (year % 19)) % 30

    print("The value of the epact is", epact)

main()
