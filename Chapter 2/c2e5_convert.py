# c2e5_convert.py
# Tony Chen

def main():
    print("╔═════╦══════╗")
    print("║ Celsius  ║ Fahrenheit ║")
    print("║------------------------║")
    for i in range(11):
        celsius = 10 * i
        fahrenheit = 9/5 * celsius + 32
        print("║   ", celsius ,"   ║  ", fahrenheit ,"   ║")
    print("╚═════╩══════╝")

main()
