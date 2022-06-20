import time

# 获取当前时间戳 返回的是一个浮点数
print('获取当前时间戳:{timestamp}'.format(timestamp=time.time()))

# 获取当前时间戳并以易读的方式表示 返回字符串
print('获取当前易读的时间形势:{timedate}'.format(timedate=time.ctime()))

# 按照指定格式返回时间信息 strftime 将一个时间戳对应为本地时间的struct_time对象 time.localtime()在括号里面还能接时间戳信息
t = time.localtime()  # 获取当前时间戳对应的本地时间的struct_time对象
print('按照指定格式返回日期信息yyyy-mm-dd HH:MM:SS:{time}'.format(time=time.strftime('%Y-%m-%d %H:%M:%S', t)))
