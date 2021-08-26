import csv

import requests
import re

url = "https://movie.douban.com/top250"

header = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

resp = requests.get(url, headers=header)

page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item".*?<span class="title">(?P<title>.*?)'
                 r'</span>.*?<p class="">.*?</br>(?P<year>.*?)&nbsp.*?<span>'
                 r'class="rating_num" proprtty="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<number>.*?)人评价</span>', re.S)

# 开始匹配
result = obj.finditer(page_content)

f = open("data.csv", mode="w")
csvwriter = csv.writer(f)

for it in result:
    # print(it.group("title"))
    # print(it.group("year").strip())  # 忽略空格
    # print(it.group("score").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    dic.update()
    csvwriter.writerow(dic.values())

f.close()
print("over")