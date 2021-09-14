import os
from functools import reduce
content = input('please input number:')
num = int(content)
sum = reduce((lambda x,y:x*y),range(1,num+1))
print(sum)

#统计一个文件里面 每个数字出现的次数情况
dict_result = {}
with open('/Users/luying/PycharmProjects/leetcode/num_file','r') as file:
    while True:
        line = file.readline().replace("\n","")
        if not line:
            break
        else:
            list_result = line.split(" ")
            for k in list_result:
                dict_result[k] = dict_result.get(k,0) + 1

max_content = None
max_times = 0
for k,v in dict_result.items():
    if max_times is None:
        max_content = k
        max_times = 1
    else:
        if v > max_times:
            max_content = k
            max_times = v

print(max_content)
print(max_times)
