import requests
import re

domain = "https://www.dytt89.com/"

resp = requests.get(domain, verify=False)  # 去掉安全验证
resp.encoding = 'gb2312'  # 指定字符集

obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<url>.*?)'", re.S)
obj3=re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td '
                r'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<child_url>.*?)"',re.S)

result1 = obj1.finditer(resp.text)

child_href_list = []
for it in result1:
    ul = it.group('ul')

    result2 = obj2.finditer(ul)
    for itt in result2:
        # 拼接子页面的地址
        child_href = domain + itt.group('url').strip("/")
        child_href_list.append(child_href)

# 获取子页面内容
for url in child_href_list:
    child_resp = requests.get(url, verify=False)
    child_resp.encoding = 'gb2312'

    result3=obj3.search(child_resp.text)
    print(result3.group("child_url"))
