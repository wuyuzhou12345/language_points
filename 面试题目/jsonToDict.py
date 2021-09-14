# 输入：JSON{"a":"aa","b":"bb","c":{"d":"dd","e":"ee"}}
# 输出：字典 {"a": "aa", "b": "bb", "d": "dd", "e": "ee"}
import json
def json_to_dict(str):
    dict_temp = json.loads(str)
    dict_result = {}
    for k,v in dict_temp.items():
        print(type(v))
        if isinstance(v,dict)  :
            for m,n in v.items():
                dict_result[m] = n
        else:
            dict_result[k] = v
    print(dict_result)

if __name__ == '__main__':
    json_to_dict('{"a":"aa","b":"bb","c":{"d":"dd","e":"ee"}}')