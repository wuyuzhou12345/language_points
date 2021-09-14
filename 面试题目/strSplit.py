from functools import reduce
str1 = 'hello ni hao hi'
print(str1.split(' '))

lista = [1,1,2,'hello']
listb = [str(x) for x in lista]
print(''.join([str(x) for x in lista]))

stu = ["张三:20", "李四:70", "王五:88", "李六:40", "王吉:55.5"]
sum = reduce(lambda x,y:x+y,[float(s.split(":")[1]) for s in stu])
print(sum)