def func_out(func):
    def func_in(*args, **kwargs):
        func(*args, **kwargs)

    return func_in


@func_out  # login = func_out(login)
def my_test(*args, **kwargs):
    print(args)
    print(kwargs)


my_test(10)
