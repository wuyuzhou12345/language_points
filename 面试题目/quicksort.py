
# def quick_sort(arr,start,end):
#     if start >= end:
#         return
#     i = start
#     j = end
#     target = arr[i]
#     while i<j:
#         while (i < j and arr[j] >= target):
#             j = j - 1
#         arr[i] = arr[j]
#         while(i<j and arr[i] < target):
#             i=i+1
#         arr[j] = arr[i]
#     arr[i] = target
#     quick_sort(arr,start,i-1)
#     quick_sort(arr,i+1,end)

def quick_sort(arr,left,right):
    i = left
    j = right
    if i >= j:
        return
    target = arr[i]
    while i<j:
        while(i<j and arr[j] >= target):
            j-=1
        arr[i] = arr[j]
        while(i<j and arr[i] < target):
            i+=1
        arr[j] = arr[i]
    arr[i] = target
    quick_sort(arr,left,i-1)
    quick_sort(arr,i+1,right)


if __name__ == '__main__':
    arr = [7,3,9,0,4,6,7]
    quick_sort(arr,0,len(arr)-1)
    print(arr)