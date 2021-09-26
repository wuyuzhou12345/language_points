def get_the_same_number(nums1,nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    result = []
    for i in nums1:
        for j in nums2:
            if i == j:
                result.append(i)
    return result


if __name__ == '__main__':
    print(get_the_same_number([1,2,2,1],[2,2]))