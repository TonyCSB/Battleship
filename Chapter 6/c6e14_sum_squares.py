# c6e14_sum_squares.py
# Tony Chen

def squareEach(nums):
    squareList = []
    for i in range(len(nums)):
        squareList.append(nums[i] ** 2)
    return squareList

def sumList(nums):
    result = 0
    
    for i in range(len(nums)):
        result = result + nums[i]

    return result

def toNumbers(strList):
    numList = []
    for i in range(len(strList)):
        numList.append(float(strList[i]))

    return numList

def main():
    print("This program reads numbers from a file and")
    print("prints the sum of their squares.\n")

    infileName = input("File name? ")

    infile = open(infileName, "r")

    numList = toNumbers(infile.readlines())
    squareList = squareEach(numList)
    result = sumList(squareList)

    infile.close()

    print()

    print("The sum of the square is:", result)

main()
