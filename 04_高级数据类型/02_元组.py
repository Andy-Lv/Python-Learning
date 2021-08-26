info_tuple = ("zhangsan", 18, 1.75)

print(info_tuple[0])  # 取值
print((info_tuple.index("zhangsan")))  # 取索引
print((info_tuple.count("zhangsan")))  # 统计计数

for my_info in info_tuple:
    print(my_info)

print("%s的年龄是%d,身高是%.02f" % info_tuple)
