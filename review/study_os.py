import os

# 常用方法 os.getcwdcwd() os.path.split(__file__) os.path.join os.path.isdir(os.getcwd()) os.path.isfile('a.txt')
# os.path.exists() os.path.basename(path) os.path.dirname(path)

# 返回文件名称
print('文件名称:{result3}'.format(result3=os.path.basename(__file__)))

# 返回文件夹名称
print('文件夹名称:{result4}'.format(result4=os.path.dirname(__file__)))

# 获取当前工作目录
print('打印当前目录:{pwd}'.format(pwd=os.getcwd()))
# 获取当前文件工作目录的文件夹和文件名，返回的是一个元组
print('获取当前文件工作目录的文件夹和文件名，返回的是一个元组:{result}'.format(result=os.path.split(os.getcwd())))
print('返回的是一个当前文件的工作目录和文件名称:{result1}'.format(result1=os.path.split(__file__)))  # 返回的是一个当前文件的工作目录和文件名称

# 获取绝对路径
print(os.path.abspath(__file__))  # 此处用的__file__是一个获取file的模仿方法

# 获取当前的系统情况 window会打印nt 对于linux/unix会打印posix
print('打印当前系统:{system}'.format(system=os.name))

# 连接目录与文件名或目录
print('连接目录和文件名信息:{result2}'.format(result2=os.path.join(os.getcwd(), 'a.txt')))

