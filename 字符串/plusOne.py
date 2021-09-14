def plus_onw(nums):
    nums = [str(i) for i in nums]
    result = int(''.join(nums)) + 1
    return list(str(result))

if __name__ == '__main__':
    print(plus_onw([1,2,3]))