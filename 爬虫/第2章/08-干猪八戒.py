import requests
from lxml import etree

url = "https://wuhan.zbj.com/search/f/?kw=saas"

resp = requests.get(url)

# 解析
tree = etree.HTML(resp.text)

# 拿到每一个服务商
divs = tree.xpath('/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div')
print(divs)
for div in divs:
    price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[1]/p/text()"))#取出中间由于高亮而未提取出的关键词saas
    com_name = div.xpath("./div/div/a[2]/div[1]/p/text()")
    location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")
    # print(price)