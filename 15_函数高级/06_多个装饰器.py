def func_out01(func01):
    print("this is func_out01")

    def func_in01():
        print("this is func_in01")
        func01

    return func_in01()


def func_out02(func02):
    print("this is func_out02")

    def func_in02():
        print("this is func_in02")
        func02

    return func_in02()


# 就近原则，谁离login近就先执行谁
@func_out01
@func_out02
def login():
    print("login")


login()
