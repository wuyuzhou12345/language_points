# 给你一个字符串 s，找到 s 中最长的回文子串。
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
# 示例 3：
#
# 输入：s = "a"
# 输出："a"
# 示例 4：
#
# 输入：s = "ac"
# 输出："a"

def find_longgest_palindrome(str):
    str_length = len(str)
    length = str_length
    while length>0:
        for i in range(str_length-length+1):
            if str[i:i+length] == str[i:i+length][::-1]:
                return str[i:i+length]
        length -= 1
    return ''

if __name__ == '__main__':
    print(find_longgest_palindrome("babad"))
    print(find_longgest_palindrome("cbbd"))
    print(find_longgest_palindrome("a"))