# 字典中键为唯一，值可以不唯一
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75,
            "weight": 70}
print(xiaoming)

print(xiaoming["name"])  # 取值

xiaoming["name"] = "xiaobizaizi"
xiaoming["girl"] = True

xiaoming.pop("name")

print(len(xiaoming))  # 统计字典键值对数量

temp = {"handsome": True}

xiaoming.update(temp)  # 合并字典，对于相同的键，就更新值

xiaoming.clear()

for k in xiaoming:
    print("%s-%s" % (k, xiaoming[k]))
