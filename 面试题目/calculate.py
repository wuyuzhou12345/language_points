from functools import reduce
content = input('please input number:')
num = int(content)
sum = reduce((lambda x,y:x*y),range(1,num+1))
print(sum)