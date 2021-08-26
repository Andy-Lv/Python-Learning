import pymysql

# 建立链接 桥梁
conn = pymysql.connect(host='localhost', port=3306, usr='root', password='mysql', database='python', charset='utf8')

# 创建游标 小弟,游标可以记录获取数据的个数
cur = conn.cursor()

# 执行sql 小弟干活
goods_name = input("请输入想要查询的商品")
sql = "select * from goods where name =%s"
# 给sql传入参数时在execute中传入
cur.execute(sql, [goods_name])

# 获取数据 卸货
data = cur.fetchall()  # 元组，每个元素都是数据库中的数据
for i in data:
    print(i)

conn.commit()

# 关闭 先关闭游标（遣散小弟），再关闭联接（炸毁桥梁）
cur.close()
conn.close()
