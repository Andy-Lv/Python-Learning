# 请求方式：GET显式提交，POST隠式提交
import requests

query = input("请输入一个你喜欢的明星：")

url = f'https://www.sogou.com/web?query={query}'  # 在浏览器地址栏里面复制的地址一定要用get

headers = {  # 伪装成为正常浏览器发出的请求
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

resp = requests.get(url, headers=headers)  # 利用一个headers处理一个小小的反爬

print(resp)
print(resp.text)  # 拿到页面源代码，但是网站会判别是不是爬虫工具或者是正常浏览器的请求
resp.close()