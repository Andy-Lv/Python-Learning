try:
    num = int(input("请输入一个整数"))
    result = 8 / num
    print(result)
except ZeroDivisionError:  # 分母为0
    print("除0错误")
except ValueError:  # 输入了字母
    print("请输入正确的整数")

except Exception as result:  # 捕获未知错误
    print("未知错误%s" % result)

else:
    print("这是没有错误才会实现的代码")
finally:
    print("无论是否正确都会执行的代码")
