import requests
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/priceDetail.html"

resp = requests.get(url)

# 解析数据
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解析器

# page.find("table", class_="hq_table")  # class是python的关键字
table = page.find("table", attrs={"class": "hq_table"})  # 和上一行一个意思,防止class被认为是关键字

trs = table.find_all("tr")[1:]  # 找到所有的"tr" 然后切片,实现不要表头行
for tr in trs:
    tds = tr.find_all("td")
    name = tds[0].text
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    date = tds[6].text
