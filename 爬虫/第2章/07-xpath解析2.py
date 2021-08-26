from lxml import etree

tree = etree.parse("a.html")  # 解析文件
result = tree.xpath('/html/body/ul/li[1]/text()')
result2 = tree.xpath("/thml/body/ol/li/a[@href='feiyuguantou']/text()")
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    # 从每个li中提取到文字
    li.xpath("./a/text()")  # 在li中继续寻找,是一个相对路径
    result3 = li.xpath("./a/@href")  # 拿到href属性值

print(tree.xpath("/html/body/ul/li/a/@href"))  # 将所有满足此条件的href打印出来

