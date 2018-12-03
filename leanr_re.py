import re

indexpat = ".*"
indexlist = re.compile(indexpat).findall('www.runoob.com');
print(indexlist)

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配