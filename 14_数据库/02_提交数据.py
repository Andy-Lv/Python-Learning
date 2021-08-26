import pymysql

# 建立链接 桥梁
conn = pymysql.connect(host='localhost', port=3306, usr='root', password='mysql', database='python', charset='utf8')

# 创建游标 小弟,游标可以记录获取数据的个数
cur = conn.cursor()

# 执行修改sql
sql = "update goods set price=99 where id=1"
cur.execute(sql)

# 获取数据
sql = "select * from goods;"
cur.execute(sql)

# 获取数据 卸货
data = cur.fetchall()  # 元组，每个元素都是数据库中的数据
for i in data:
    print(i)

# 要修改数据库需要进行提交操作，否则不会真正的修改
conn.commit()

# 关闭 先关闭游标（遣散小弟），再关闭联接（炸毁桥梁）
cur.close()
conn.close()
