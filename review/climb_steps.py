def climb_step(num):
    a,b = 1,1
    while num>0:
        a,b = b,a+b
        num -= 1
        yield a

if __name__ == '__main__':
    result = 0
    for i in climb_step(5):
        result = i

    print(result)

