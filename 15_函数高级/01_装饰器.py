# 装饰器：在不修改原有的函数的代码的前提下给函数增加新的功能

def func_out(func):
    def func_in():
        print("验证")
        func()

    return func_in


@func_out  # login = func_out(login)
def login():
    print("登陆")


login()  # 调用login就相当于调用闭包中的内层函数func_in
# 外层函数的参数  func=>原始的login
