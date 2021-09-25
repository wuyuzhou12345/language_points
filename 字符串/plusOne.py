def plus_onw(nums):
    nums = [str(i) for i in nums]
    result = int(''.join(nums)) + 1
    return list(str(result))

def plus(nums):
    for index,value in enumerate(nums):
        nums[index] = value + 1
    return nums

if __name__ == '__main__':
    print(plus_onw([1,2,3]))
    print(plus([1,2,3]))