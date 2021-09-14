#深拷贝和浅拷贝的区别
#深拷贝本质是拷贝了所有的父对象及其子对象 copy.deepcopy()，是递归拷贝
#浅拷贝本质是只拷贝了父对象，不会拷贝其内部的子对象
#浅拷贝的几种方式 copy.copy() [1:3]切片 [x for x in range(5)]列表表达式 list(a)工厂函数
import copy
import copy
a=[1,2,3,4,5,['a','b']]
#原始对象
b=a#赋值，传对象的引用
c=a[:]#对象拷贝，浅拷贝
d=copy.deepcopy(a)#对象拷贝，深拷贝
print("a=",a,"    id(a)=",id(a),"id(a[5])=",id(a[5]))
print("b=",b,"    id(b)=",id(b),"id(b[5])=",id(b[5]))
print("c=",c,"    id(c)=",id(c),"id(c[5])=",id(c[5]))
print("d=",d,"    id(d)=",id(d),"id(d[5])=",id(d[5]))
print("*"*70)

print("a=",a,"    id(a)=",id(a),"id(a[4])=",id(a[4]))
print("b=",b,"    id(b)=",id(b),"id(b[4])=",id(b[4]))
print("c=",c,"    id(c)=",id(c),"id(c[4])=",id(c[4]))
print("d=",d,"    id(d)=",id(d),"id(d[4])=",id(d[4]))
print("*"*70)

a.append(6)#修改对象a
a[5].append('c')#修改对象a中的['a','b']数组对象
print("a=",a,"    id(a)=",id(a),"id(a[5])=",id(a[5]))
print("b=",b,"    id(b)=",id(b),"id(b[5])=",id(b[5]))
print("c=",c,"    id(c)=",id(c),"id(c[5])=",id(c[5]))
print("d=",d,"    id(d)=",id(d),"id(d[5])=",id(d[5]))
