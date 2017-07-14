# c8e12_degree_days_file.py
# Tony Chen

def main():
    print("This program calculates heating degree-days and")
    print("cooling degree-dats for a year of average daily")
    print("(Fahrenheit) temperature values, read from a text")
    print("file.\n")

    infileName = input("Filename? ")

    infile = open(infileName, "r")

    line = infile.readline()
    cool = 0
    heat = 0

    while line != "":
        for n in line.split():
            x = float(n)
            if x < 60:
                heat = heat + 60 - x
            elif x > 80:
                cool = cool + x - 80
        line = infile.readline()

    infile.close()

    print("\nHeating degree-days:{0:>7.2f}".format(heat))
    print("Cooling degree-days:{0:>7.2f}".format(cool))

main()

