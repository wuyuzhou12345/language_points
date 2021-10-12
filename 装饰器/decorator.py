import functools
import time

def logger(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('method_name:{},execute_time:{}'.format(func.__name__,end_time-start_time))
    return wrapper

@logger
def print_content(content):
    print(content)

if __name__ == '__main__':
    print_content('hi')