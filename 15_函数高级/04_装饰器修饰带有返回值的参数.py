def func_out(func):
    def func_in():
        ret = func()  # 函数中没有return,证明函数没有返回值，返回None
        return ret

    return func_in


@func_out  # login = func_out(login)
def my_test():
    return 100


a = my_test
print(a)
