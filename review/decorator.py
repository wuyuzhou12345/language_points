import functools
import time

#闭包 两个函数的互相嵌套，内部函数持有外部函数的引用，外部函数返回内部函数的引用
#装饰器主要用来修饰函数，在对函数无侵入的情况下，进行一个增强的作用

def logger(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("method {} execute time ".format(func.__name__,end_time-start_time))
    return wrapper

def logger_with_param(debug='info'):
    def outer_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args,**kwargs):
            print("debug level {}".format(debug))
            func(*args,**kwargs)
        return inner_wrapper
    return outer_wrapper


@logger_with_param('info')
@logger
def say_hi(content):
    print(content)

if __name__ == '__main__':
    say_hi('hi')