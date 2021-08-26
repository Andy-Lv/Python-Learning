name_list = ["张三", "李四", "王五"]

print(name_list[0])

print(name_list.index("王五"))  # 知道数据的内容，想知道数据所在的位置

name_list[0] = "zhangsan"  # 修改元素

name_list.append("wangxiaoer")  # 尾部添加

name_list.insert(1, "xiaobizaizi")  # 在任意位置添加

temp_list = ["孙悟空", "猪八戒", "沙僧"]
name_list.extend(temp_list)  # 相当于name_list += temp_list

name_list.remove("zhangsan")  # 删除指定数据
name_list.pop()  # 删除最后一个元素
name_list.pop(3)  # 也可以根据元素位置索引删除
name_list.clear()  # 删除所有元素
list_len = len(name_list)  # 统计列表长度

name_list.count("张三")  # 统计元素出现的次数

num_list = [4, 5, 3, 6, 2, 1, 8]

num_list.sort()  # 从小到大排序
num_list.sort(reverse=True)  # 从大到小排列
num_list.reverse()  # 反转

for my_name in name_list:
    print("my name is %s" % my_name)
