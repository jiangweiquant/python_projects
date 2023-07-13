import re
#findall(r'正则表达式','字符串')返回列表[列表效率不是很高]
# phone_num = re.findall(r'\d{3}-\d{8}|\d{4}-\{7,8}', '第一个电话号码：180-81208401,第二个电话号码:180-11606670')
# print(phone_num)

# #finditer返回迭代器####最重要
# phone_num = re.finditer(r'\d{3}-\d{8}|\d{4}-\{7,8}', '第一个电话号码：180-81208401,第二个电话号码:180-11606670')
# print(phone_num)
# for i in phone_num:
#     print(i)
#     print(i.group())

# #search返回match对象[找到一个就返回]，从match对象里获取内容.group()
# phone_num = re.search(r'\d{3}-\d{8}|\d{4}-\{7,8}', '第一个电话号码：180-81208401,第二个电话号码:180-11606670')
# print(phone_num.group())
# print(phone_num.group())

#match[从头匹配]
# phone_num = re.match(r'\d{3}-\d{8}|\d{4}-\{7,8}', '180-81208401,第二个电话号码:180-11606670')
# print(phone_num.group())

# #预加载正则表达式
# obj = re.compile(r'\d{3}-\d{8}|\d{4}-\{7,8}')#这个正则反复用到
# ret = obj.finditer('第一个电话号码：180-81208401,第二个电话号码:180-11606670')
# for i in ret:
#     print(i.group())
# ret = obj.findall('teacher is 20 ages,and his numer is 132-12203860')
# print(ret)


# (?P<自定义名字>正则表达式) 可以单独从正则匹配到的内容中进一步提取内容
s = """
<div class='a'><span id='1'>爬虫</span></div>
<div class='b'><span id='2'>进程</span></div>
<div class='c'><span id='3'>线程</span></div>
<div class='d'><span id='4'>mysql</span></div>
<div class='e'><span id='5'>redis</span></div>
"""
obj = re.compile(r"<div class='(?P<class>.*?)'><span id='(?P<id>\d+)'>(?P<content>.*?)</span></div>", re.S)#re.S让.能匹配换行符
result = obj.finditer(s)
for i in result:
    print(i.group('class'))
    print(i.group('id'))
    print(i.group('content'))
