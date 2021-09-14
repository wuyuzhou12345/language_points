def is_palindrome(num):
    if(num<0):
        return False
    else:
        if int(''.join(list(str(num))[::-1])) == num:
            return True
    return False

if __name__ == '__main__':
    print(is_palindrome(121))
    print(is_palindrome(-121))