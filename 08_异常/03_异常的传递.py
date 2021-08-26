# 函数内出现错误时，如果函数没有处理，就会传回调用他的主函数
def demo1():
    return int(input("请输入一个整数"))


def demo2():
    return demo1()


# 利用传递回主函数的特性在主函数中捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误%s" % result)
