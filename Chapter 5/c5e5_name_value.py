# c5e5_name_value.py
# Tony Chen

def main():
    print("This program calculates the numeric value")
    print("of a sing name provided as input.\n")
    
    name = input("Please enter the name: ")

    name = name.lower()

    value = 0

    for ch in name:
        n = ord(ch) - 96
        value = n + value

    print("The value is:", value)

main()
