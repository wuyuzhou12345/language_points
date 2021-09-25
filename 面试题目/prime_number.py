def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

if __name__ == '__main__':
    result = []
    for i in range(101,200):
        if is_prime(i):
            result.append(i)
    print(result)
    print(7%4)
