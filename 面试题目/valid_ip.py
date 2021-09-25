import re
'''
判断一个字符串是不是一个合法的ip
合法的ip第一位不是为0,但是0.0.0.0表示的本机ip 127.0.0.1也表示的是相关的本机ip
'''
def is_valid_ip(str):
    nums = str.split('.')
    if(len(nums) != 4) :
        return False
    for i,v in enumerate(nums):
        result = re.findall(r'\d+',v,re.M|re.I)
        if not result:
            return False
        if int(v)> 255 or int(v)<0:
            return False
        if i == 0 and int(v) == 0:
            return False

    if nums[0] == '127':
        if nums[1] == '0' and nums[2] == '0' and nums[3] == '1':
            return True
        else:
            return False
    return True

if __name__ == '__main__':
    print(is_valid_ip('0.255.255.255'))