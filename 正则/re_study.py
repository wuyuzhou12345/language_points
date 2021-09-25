import re
content = "dogs are smarter than cats 1 456"
# re.search(r‘(.*)sdfjd(.*)’,str,re.M|re.I)
s = re.search(r"(.*)are(.*)than(.*)",content,re.M)
print(s.group(1))

m = re.findall(r'\w{4,}',content,re.M)
print(m)
