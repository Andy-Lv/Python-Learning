# 1 拿到主页面源代码,然后提取子页面的链接地址
# 2 通过href找到子页面内容,从子页面找到图片的下载地址
# 3 下载图片

import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'

# 吧源代码交给bs4
main_page = BeautifulSoup(resp.text, "html.parser")
a_list = main_page.find("div", attrs={"class": "TypeList"}).find_all("a")  # 把范围第一次缩小,找到所有的<a>标签
resp.close()

for a in a_list:
    href = "https://umei.cc/" + a.get('href')
    # print(href)
    #   拿到子页面源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    #     从子页面中拿到下载路径
    child_page = BeautifulSoup(child_page_text, "html.parser")
    img = child_page.find("p", attrs={"align": "center"}).find("img")

    src = img.get("src")

    #     下载图片
    img_resp = requests.get(src)
    img_resp.content  # 这里拿到的是字节

    img_name = "img/" + src.split("/")[-1]  # 拿到url最后一个"/"以后的内容
    with open(img_name, mode="wb") as f:
        f.write(img_resp.content)
        print("download the " + img_name + " successful")
        time.sleep(1)

print("all over")
