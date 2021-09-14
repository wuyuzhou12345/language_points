#tuple的常用的方法 for in 进行迭代 len()获取长度 tuple[:-1]切片 tuple.count tuple.index(),tuple(list)
#tuple和dict的区别
#tuple是不可变的，而dict是可变的，不可变指如果值发生了改变，指向的地址也会相应发生改变
#dict中存储类型是key-value对是无序的，但是tuple中是有序的，可以通过index下标获取元祖中的内容,dict中的key都是不能重复的，但是tuple中的元素是可以有相同的元素的
tuple_a = ('a',1,{'Content-Type':'application/json'},1)
tuple_b = ('b',2,{'Content-Type':'application/formed'})
for i in tuple_a:
    print(i)

print(tuple_a.count('a'))
print(tuple_a.index('a'))
print(len(tuple_a))

print(tuple_a[1:])
tuple_c = tuple_a + tuple_b
print(tuple_c)