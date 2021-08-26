from lxml import etree

xml = """
<html>

   <head>

   <title>HTML语言中颜色的不同表示方法</title>

   </head>

   <body>

   <font color="red">静夜思</font><br><!红色>

   <font color="#008000">窗前明月光</font><br><!绿色>

   <font color="rgb(0,0,255)">疑是地上霜</font><br><!蓝色>

   <font color="#ffff00">举头望明月</font><br><!黄色>

   <font color="#800000">低头思故乡</font><!栗色>

   </body>

</html>
"""

tree = etree.XML(xml)

tree.xpath("/head")  # /表示层级关系,第一个/表示根节点,
result = tree.xpath("/head/title/text()")  # text()拿文本,如果有多个,则将所有满足条件的储存到一个元组中
result2 = tree.xpath("/head//title/text()")#将head的所有title后代都用文本的形式提取出来
result3 = tree.xpath("/head/*/title/text()")#将head所有孙子中的title提取出来,*占用一个层级