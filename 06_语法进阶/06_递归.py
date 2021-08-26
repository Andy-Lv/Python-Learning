def sum_num(num):
    print(num)

    sum_num(num - 1)

    # 出口
    if num == 1:
        return


sum_num(3)


def sum_number(num):
    if num == 1:
        return 1
    temp = sum_number(num - 1)
    return temp + num


sum_number(6)
