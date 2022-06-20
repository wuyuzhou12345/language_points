import sys

# 执行这个py文件的时候 请带入参数情况 python3 study_sys.py a b c
print('打印传入的参数情况:{argvs}'.format(argvs=sys.argv))  # 这边注意第一个参数是文件名称不包含路径 第二个参数是a
print('打印python环境配置变量信息:{path}'.format(path=sys.path))

# 打印输入的内容
line = sys.stdin.readline()
print('输入的内容情况为:{content}'.format(content=line))
