i = 1

while i <= 5:
    print("你好帅")  # 如果不想换行，可以print("你好帅",end="")
    i += 1
print("打印结束，一共打印了%d次" % i)

# 9x9乘法表
raw = 1
lie = 1
while raw <= 9:
    while lie <= raw:
        print("%dx%d=\t%d" % (raw, lie, raw * lie), end=" ")
        lie += 1
    print("")
    raw += 1
    lie = 1
