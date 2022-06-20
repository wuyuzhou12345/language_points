import random

print('生成一个0-1之间的浮点数:{num1}'.format(num1=random.random()))  # 返回随机生成的一个实数，它在[0,1)范围内。

print('产生1到10的一个整数型随机数:{num2}'.format(num2=random.randint(1, 10)))  # 产生1到10的一个整数型随机数

print('生成从1到100的间隔为2的随机整数:{num3}'.format(num3=random.randrange(1, 100, 2)))  # 生成从1到100的间隔为2的随机整数

a = [1, 3, 5, 6, 7]  # 将序列a中的元素顺序打乱
random.shuffle(a)
print('将a中的元素打乱:{list}'.format(list=a))

# 随机选取字符串：
print(random.choice(['剪刀', '石头', '布']))

# 多个字符中生成指定数量的随机字符：
print(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))
