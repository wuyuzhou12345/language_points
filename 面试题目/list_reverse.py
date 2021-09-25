list_a = [1,2,3,4,5,6,7,7]
list_b = []
list_c = []
length = len(list_a)
# while length>0:
#     list_b.append(list_a[length-1])
#     length-=1
# print(list_b)


#
# for i in list_a:
#     if i not in list_c:
#         list_c.append(i)
# print(list_c)

while length>0:
    list_b.append(list_a[length-1])
    length-=1
print(list_b)
