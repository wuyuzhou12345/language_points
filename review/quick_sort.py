def quick_sort(array,start,end):
    if start >= end:
        return
    target = array[start]
    i = start
    j = end
    while i<j:
        while i<j and array[j] > target:
            j-=1
        array[i] = array[j]
        while i<j and array[i] <= target:
            i+=1
        array[j] = array[i]
    array[i] = target
    quick_sort(array,start,i-1)
    quick_sort(array,i+1,end)


if __name__ == '__main__':
    arr = [6,4,6,9,0,2]
    quick_sort(arr,0,len(arr)-1)
    print(arr)