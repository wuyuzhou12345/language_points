import functools
def logger(debug):
    def outer_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args,**kwargs):
            func(*args,**kwargs)
            if debug == 'info':
                print('method_name:{},debug_info:{}'.format(func.__name__,'info'))
            else:
                print('method_name:{},debug_info:{}'.format(func.__name__, 'error'))
        return inner_wrapper
    return outer_wrapper


@logger(debug='error')
def print_content(content):
    print(content)

if __name__ == '__main__':
    print_content('hi')