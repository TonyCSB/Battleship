# c3e5_coffee.py
# Tony Chen

def main():
    print("This program calculates the cost of a coffee order.")
    print("The Konditorei coffee shop sells coffee at $10.50 a")
    print("pound plus the cost of shipping, which is $0.86 per")
    print("pound plus $1.50 fixed cost for overhead.")

    print()
    
    coffee = float(input("Please enter the weight of the coffee in pound: "))
    
    cost = (10.50 + 0.86) * coffee + 1.50

    print()
    
    print("The cost of the order is", cost)

main()
