def max_sub_array(nums):
    result = []
    for i in range(len(nums)):
        if i < len(nums) - 1:
            for j in range(i+1,len(nums)):
                result.append(int(sum(nums[i:j+1])))
    return max(result)



if __name__ == '__main__':
    print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
    print(type(sum([-2,1,-3,4,-1,2,1,-5,4])))