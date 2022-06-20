# 常用的有OrderedDict有序字典 和 Counter计数
import collections
import random

# python的基础数据类型中的字典类型分为：无序字典和有序字典 但在py3.6 以后，字典默认为有序了
my_dict = dict()
my_dict['name'] = 'lowman'
my_dict['age'] = 45
my_dict['girl'] = 'Thailand'
my_dict['money'] = 998
my_dict['house'] = None

for key, value in my_dict.items():
    print(key, value)

print('*' * 50)

my_order_dict = collections.OrderedDict()
my_order_dict['name'] = 'lowman'
my_order_dict['age'] = 45
my_order_dict['girl'] = 'Thailand'
my_order_dict['money'] = 998
my_order_dict['house'] = None

for key, value in my_order_dict.items():
    print(key, value)

print('*' * 50)

num_list = []
for m in range(10):
    x = random.randint(1, 10)  # 产生1到10的一个整数型浮点数
    num_list.append(x)

print(num_list)
count = collections.Counter(num_list)
print(count.most_common(1))  # most_common(n)用于显示前n个最多的元素
