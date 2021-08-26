str1 = "hello"
str2 = 'my name is "big xigua"'

print(str1[4])

for char in str2:
    print(char)

print(len(str))

print(str1.count("llo"))  # 统计某一个小字符串出现的次数

print(str1.index("llo"))  # 统计某一个小字符串出现的位置

print(str1.startswith("he"))  # True
print(str1.endswith("lo"))  # True

str1.replace("ll", "python")

poem = {"登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"}
for poem_str in poem:
    print(poem_str.center(10))
for poem_str in poem:
    print(poem_str.ljust(10, " "))
for poem_str in poem:
    print(poem_str.rjust(10, " "))

poem_str = "登鹳雀楼\t 王之涣 \t白日依山尽\t \n黄河入海流\t\t 欲穷千里目\n更上一层楼"
poem_list = poem_str.split()  # 以空格为分界线，将元素保存为一个列表
result = " ".join(poem_list)

result[-1::-1]  # 字符串逆序
