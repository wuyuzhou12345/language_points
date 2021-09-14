#map,reduce,filter中经常会使用lambda匿名函数
#map是映射式的
#reduce是累积式的
#filter进行简单的过滤操作

a = filter(lambda x:x%2 ==0,range(5))
print(a)
print(list(a))

b = [1,2,4]
c = [3,6,9]
d = map(lambda m,n:m+n,b,c)
print(list(d))