def input_password():
    # 提示输入密码
    pwd = input("请输入密码")
    # 判断密码长度，如果小于8就返回错误
    if len(pwd >= 8):
        return pwd
    print("主动抛出异常")
    # 创建异常对象，可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 抛出异常
    raise ex


try:
    # 提示用户输入密码
    print(input_password())
except Exception as result:
    print("未知错误%s" % result)
