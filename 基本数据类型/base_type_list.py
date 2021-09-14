#list是可变的，即列表中的值发生改变，但是所指向的地址不会发生改变
#list和tuple的区别，list是可变的，tuple是不可变的
#list和dictionary的区别,dictionary是无序的，list是有序的，且list中的内容可以重复，但是dictionary中的key是唯一不能相同的
#list中的方法 切片[::-1]倒序 [1:] extend进行列表合并 append列表中元素添加 index count remove
list_a = [1,'a','b',2,3,'a',5]
print(list_a)
list_a.index('a')
list_a.count('a')
list_a.append(6)
print(list_a)

list_b = [2,3,4,5]
list_a.extend(list_b)
print(list_a)

print(list_a.count(2))
print(list_a)
