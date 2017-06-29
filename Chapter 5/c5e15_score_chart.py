# c5e15_score_chart.py
# Tony Chen

from graphics import *

def main():
    print("This program could read data from a file that contains")
    print("numbers in the range 0-10, and then draw a vertical bar")
    print("chart with a bar for each possible score (0-10).\n")

    infileName = input("File name? ")

    infile = open(infileName, "r")

    numberList = "ABCDEFGHIJK"

    number = ""

    for n in infile:
        number = number + numberList[int(n)]

    infile.close()

    n0 = number.count("A")
    n1 = number.count("B")
    n2 = number.count("C")
    n3 = number.count("D")
    n4 = number.count("E")
    n5 = number.count("F")
    n6 = number.count("G")
    n7 = number.count("H")
    n8 = number.count("I")
    n9 = number.count("J")
    n10 = number.count("K")

    win = GraphWin("Quiz Score Histogram", 500, 300)
    win.setCoords(-0.5, -1, 11.5, 10)

    for i in range(11):
        Text(Point(0.5 + i, -0.5), i).draw(win)
        
    Rectangle(Point(0.2, 0), Point(0.8, n0)).draw(win)
    Rectangle(Point(1.2, 0), Point(1.8, n1)).draw(win)
    Rectangle(Point(2.2, 0), Point(2.8, n2)).draw(win)
    Rectangle(Point(3.2, 0), Point(3.8, n3)).draw(win)
    Rectangle(Point(4.2, 0), Point(4.8, n4)).draw(win)
    Rectangle(Point(5.2, 0), Point(5.8, n5)).draw(win)
    Rectangle(Point(6.2, 0), Point(6.8, n6)).draw(win)
    Rectangle(Point(7.2, 0), Point(7.8, n7)).draw(win)
    Rectangle(Point(8.2, 0), Point(8.8, n8)).draw(win)
    Rectangle(Point(9.2, 0), Point(9.8, n9)).draw(win)
    Rectangle(Point(10.2, 0), Point(10.8, n10)).draw(win)

    win.getMouse()
    win.close()

main()
