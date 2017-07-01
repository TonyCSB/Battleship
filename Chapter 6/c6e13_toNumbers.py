# c6e13_toNumbers.py
# Tony Chen

def toNumbers(strList):
    numList = []
    for i in range(len(strList)):
        numList.append(float(strList[i]))

    return numList

def main():
    strList = ["1", "2", "2.1312", "14124123.123121"]
    numList = toNumbers(strList)

    print(strList)
    print(numList)

main()
