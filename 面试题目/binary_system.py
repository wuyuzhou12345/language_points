def to_binary(num):
    result = []
    while num >= 1:
        yushu = num%2
        result.append(yushu)
        num = num//2
    return ''.join([str(i) for i in result[::-1]])

if __name__ == '__main__':
    print(to_binary(4))
