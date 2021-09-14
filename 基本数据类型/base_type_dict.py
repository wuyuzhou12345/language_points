#python的基本数据类型，主要包含numbers，string，tuple，list，dictionary，set
#其中 tuple，string，numbers都是不可变的数据类型
#list，dictionary，set都是可变的数据类型
#所谓的可变指的是变量的值变了，则对应的地址也会发生改变，不可变指的是变量的值变了，对应的地址也会相应的发生改变
#dictionary的常用方法:get,items,update,keys,values,dict(dict1,**dict2)进行合并,pop对dict中的某个key进行删除操作

dict_header = {
    "Content-Type":"application/json",
    "Cookie":"token:123456789"
}

dict_content = {
    "name":"luying",
    "age":20
}

for k,v in dict_header.items():
    print(k,v)

for k in dict_header.keys():
    print(k)

for v in dict_header.values():
    print(v)

#两个字典的合并
dict_new = dict(dict_header,**dict_content)
print(dict_new)

print(dict_new.get("Content-Type1",'aaaa'))
dict_new['Content-Type'] = 'bbb'
dict_new.update({'Content-Type':'ccc'})
dict_new.pop('Content-Type')
for k,v in dict_new.items():
    print(k,v)

