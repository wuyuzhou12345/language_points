import re
def is_valid_brackets(str):
    while "()" in str  or "[]" in str or "{}" in str:
        str = str.replace("()","")
        str = str.replace("[]","")
        str = str.replace("{}","")
    return str == ""

if __name__ == '__main__':
    print(is_valid_brackets("()[]{})"))
    print(is_valid_brackets("()()()"))
    print(is_valid_brackets("([])"))