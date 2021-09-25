import functools
import time

def time_log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('{} execute time:{}'.format(func.__name__,end_time-start_time))
    return wrapper

def logger(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('method_name:{},execute_time:{}'.format(func.__name__,end_time-start_time))
    return wrapper

@logger
def sort_nums(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    print(nums)


if __name__ == '__main__':
    print(sort_nums([3,8,5,7,0]))