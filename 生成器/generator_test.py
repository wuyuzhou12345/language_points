#产生生成器的两种方式，一种是包含yield的函数是生成器，还有一种是（）类似于列表推导式
#使用生成器主要用在大文件，但是不想占用太多的空间，通过生成器可以解决内存问题
def read_big_file(path):
    with open(path,'r') as file:
        while True:
            content = file.readline().replace('\n','')
            if not content:
                break;
            else:
                yield content.split(' ')[0]

if __name__ == '__main__':
    for i in read_big_file('//big_file.txt'):
        print(i)