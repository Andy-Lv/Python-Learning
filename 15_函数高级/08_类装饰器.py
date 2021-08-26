class Func:
    def __init__(self, fn):
        # fn就是用来保存原始的被装饰的函数
        self._fn = fn

    def __call__(self):
        print("this is call")
        # 原始的被装饰的函数
        self._fn()


@Func  # my_test = Func(my_test)
def my_test():
    print("mytest")


my_test()
