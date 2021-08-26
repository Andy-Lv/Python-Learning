# 爬虫：通过编写程序获取到互联网上的资源
# 百度
# 需求：用程序模拟浏览器，输入一个网址，从该网址获取到资源或内容
# python搞定以上需求特别简单
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)
print(resp.read().decode("utf-8"))

with open("mybaidu.html", mode="w")as f:  # spider the baidu.com code in baidu.html
    f.write(resp.read().decode("utf-8"))
print("over")
