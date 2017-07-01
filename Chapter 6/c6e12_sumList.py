# c6e12_sumList.py
# Tony Chen

def sumList(nums):
    result = 0
    
    for i in range(len(nums)):
        result = result + nums[i]

    return result

def main():
    nums = [1, 2, 3, 4, 5, 6]
    result = sumList(nums)
    print(nums, "\n", result)

main()
