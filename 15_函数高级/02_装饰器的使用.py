import time


def func_out(func):
    def func_in():
        start = time.time()
        func()  # 储存了被装饰的函数
        end = time.time()
        print("使用时间为：", end - start)

    return func_in()


@func_out
def my_test():
    for i in range(1000):
        print(i)


if __name__ == '__main__':
    my_test()
