def func_out(func):
    def func_in(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret

    return func_in


@func_out  # login = func_out(login)
def my_test(*args, **kwargs):
    print(args)
    print(kwargs)


a = my_test(10)
print(a)
