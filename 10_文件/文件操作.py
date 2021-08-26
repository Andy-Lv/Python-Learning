# 读取文件
file = open("README")
text = file.read()  # 文件指针会移动到文件末尾，再打开后就不会读取到任何东西
print(text)
file.close()

# "r"只读，文件指针在文件开头，默认，文件不存在会抛出异常
# "w"只写，文件存在会被覆盖，如果不存在则会创建文件
# "a"追加，文件存在则文件指针会被放在文件末尾，如果不存在则创建文件
# "r+"读写，指针在开头，文件不存在则抛出异常
# "w+"读写，文件存在会被覆盖，如果不存在则会创建文件
# "a+"读写，文件存在则文件指针会被放在文件末尾，如果不存在则创建文件
file = open("README", "w")
file.write("hello")
file.close()



file=open("README")
while True:
    text=file.readline()#只读取一行
    if not text:
        break

    print(text,end="")

file.close()