# c6e11_squareEach.py
# Tony Chen

def squareEach(nums):
    squareList = []
    for i in range(len(nums)):
        squareList.append(str(nums[i]) + " " + str(nums[i] ** 2) + "\n")

    square = "".join(squareList)
    return square

def main():
    numberList = [1, 2, 3, 4, 5, 6]
    result = squareEach(numberList)
    print(result)

main()
