# Regular Expression，正则表达式，一种使用表达式的方式对字符串进行匹配的语法规则
# 正则表达式测试：https://tool.oschina.net/regex
# 元字符：具有固定含义的特殊符号

import re

# findall 匹配字符串中所有的符合正则的内容
lst = re.findall(r"\d+", "我的电话号码是：10086,我女朋友的电话号码是：10010")  # 前面加一个r,转义
print(lst)

# finditer 匹配字符串中所有内容，返回的是迭代器
it = re.finditer(r"\d+", "我的电话号码是：10086,我女朋友的电话号码是：10010")
for i in it:
    print(i)
    print(i.group())

# search 返回的是match对象 ,拿数据需要group
s = re.search(r"\d+", "我的电话号码是：10086,我女朋友的电话号码是：10010")
print(s.group())

# match从头开始匹配
a = re.match(r"\d+", "我的电话号码是：10086,我女朋友的电话号码是：10010")
print(a.group())

# 预加载正则表达式
obj = re.compile(r"\d+")

ret = obj.finditer("我的电话号码是：10086,我女朋友的电话号码是：10010")
for i in ret:
    print(i)
    print(i.group())

s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jilin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S)  # re.S 让"."能匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("id"))
    print(it.group("wahaha"))
