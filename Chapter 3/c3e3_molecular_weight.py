# c3e3_molecular_weight.py
# Tony Chen

def main():
    print("This program computes the molecular weight of a")
    print("carbohydrate, based on the number of Hydrogen, Carbon")
    print("and Oxygen atoms in a molecule of the compound.")
    
    h = int(input("Please enter the number of hydrogen atoms: "))
    c = int(input("Please enter the number of carbon atoms: "))
    o = int(input("Please enter the number of oxygen atoms: "))
    
    molecularWeight = h * 1.00794 + c * 12.0107 + o * 15.9994
    print("The molecular weight of the carbohydrate is", molecularWeight)

main()
