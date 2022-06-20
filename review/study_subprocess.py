# subprocess 模块允许我们启动一个新进程，并连接到它们的输入/输出/错误管道，从而获取返回值
# subprocess 模块首先推荐使用的是它的 run 方法，更高级的用法可以直接使用 Popen 接口
# https://www.runoob.com/w3cnote/python3-subprocess.html

# popen 是subprocess的核心，子进程的创建和管理都是靠它来处理的

import subprocess

# -------pOpen方法-------------
p = subprocess.Popen('ls -l', shell=True)  # 这里也可以使用 p = subprocess.Popen(['ls', '-cl']) 来创建子进程。
p.returncode
p.wait()
p.returncode


# Popen 对象方法
# poll(): 检查进程是否终止，如果终止返回 returncode，否则返回 None。
# wait(timeout): 等待子进程终止。
# communicate(input,timeout): 和子进程交互，发送和读取数据。
# send_signal(singnal): 发送信号到子进程 。
# terminate(): 停止子进程,也就是发送SIGTERM信号到子进程。
# kill(): 杀死子进程。发送 SIGKILL 信号到子进程。

def cmd(command):
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    subp.wait(2)
    # print(subp.poll())
    if subp.poll() == 0:
        # print(subp.communicate())
        print(subp.communicate()[1])
    else:
        print("失败")


cmd("pwd")
cmd("java -version")
cmd("exit 1")


# ------run方法-------------
print('*'*50)
subprocess.run(["ls", "-l", "/dev/null"])
