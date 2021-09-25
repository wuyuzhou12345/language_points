import os

#os.chdir(path)切换文件目录
#os.listdir()查看当前目录的文件情况 只会返回相关的文件名情况
#os.path.join(path,file)将目录和文件进行粘连
#os.path.split(path)可以将根目录和文件名进行切分
#os.path.isfile os.path.isdir判断是文件还是文件夹
#os.rmdir os.remove 删除一个文件夹和删除一个文件
#os.system(linux_command) 可以执行一个linux命令

result = 0
list = []

def calculate_python_files(path):
    os.chdir(path)
    files = os.listdir()
    if not files:
        return
    for file in files:
        print(file)
        if os.path.isfile(os.path.join(path,file)):
            if file.count('.py') <= 0:
                global result
                result += 1
                list.append(os.path.join(path,file))
        if os.path.isdir(os.path.join(path,file)):
            calculate_python_files(os.path.join(path,file))

def remove_child_files(path):
    os.chdir(path)
    files = os.listdir()
    if not files:
        return
    for file in files:
        print(file)
        if os.path.isdir(os.path.join(path,file)):
            remove_child_files(os.path.join(path,file))
        elif os.path.isfile(os.path.join(path,file)):
            print("file is delted:" + os.path.join(path,file))
            os.remove(os.path.join(path,file))

def remove_child_dirs(path):
    os.chdir(path)
    files = os.listdir()
    if not files:
        return
    for file in files:
        if os.path.isdir(os.path.join(path,file)):
            print(os.path.join(path,file))
            os.rmdir(os.path.join(path,file))

if __name__ == '__main__':
    remove_child_files('/Users/luying/PycharmProjects/leetcode/redis操作/test')
    remove_child_dirs('/Users/luying/PycharmProjects/leetcode/redis操作/test')
