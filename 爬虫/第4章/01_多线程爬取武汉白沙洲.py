# 1 提取单个页面数据
# 2 上线程池,多个页面同时抓取

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f = open("data.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)


def download_on_page(url):
    resp = requests.get(url)
    # print(resp.text)
    html = etree.HTML(resp.text)
    print(html)
    trs = html.xpath('/html/body/form/table[4]/tbody/tr/td[3]/table[5]/tr')
    print(trs)
    # trs = table.xpath("./tr")[0:]
    for tr in trs:
        txt = tr.xpath("./td/text()")
        print(txt)
        # 对数据进行处理
        txt = (item.relpace("\\", "").replace("/", "") for item in txt)

        csv.writerow(txt)

    print(url, "提取完毕")


if __name__ == '__main__':
    for i in range(1, 3):  # 效率极其底下
        download_on_page(f"http://www.whbsz.com.cn/Price.aspx?PageNo={i}")


    # 利用线程池提高线程
    # with ThreadPoolExecutor(2) as t:
    #     for i in range(1, 3):
    #         t.submit(download_on_page, f"http://www.whbsz.com.cn/Price.aspx?PageNo={i}")
    #
    # print("全部下载完毕")
