# 参数名前加“*”可以接收元组
# 参数名前加“**”可以接收字典
def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


demo(1)
demo(1, 2, 3, 4)  # num=1,其他的是元组
demo(1, 2, 3, 4, name="xiaoming")  # num=1,其他的数字是元组，最后是字典


# 多值参数求和
def sum_num(*args):
    num = 0
    for n in args:
        num += n
    return num


result = sum_num(1, 2, 3, 4)
