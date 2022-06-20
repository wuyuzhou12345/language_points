import re

content = "dogs are smarter than cats 1 456"
# re.search(r‘(.*)sdfjd(.*)’,str,re.M|re.I)
s = re.search(r"(.*)are(.*)than(.*)", content, re.M)
print(s.group(1))

# {n} 重复n次 {n,}重复n次或者更多次 {n,m}重复n到m次
m = re.findall(r'\w{4,}', content, re.M) #\w在正则里面表示字母或数字或下划线或汉字  \W匹配特殊字符非字母非汉字非数字 \d匹配数字 \D匹配非数字
print(m)
