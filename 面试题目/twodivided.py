def two_divide(nums,target):
    if(len(nums) <=0):
        return False
    mid = len(nums) // 2
    print(mid)
    if target == nums[mid]:
        return True
    elif target > nums[mid]:
       return two_divide(nums[mid+1:],target)
    else:
        return two_divide(nums[:mid],target)

if __name__ == '__main__':
    print(two_divide([1,5,8,10,13,16,19,30],19))