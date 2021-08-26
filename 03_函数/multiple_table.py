def multiple_table():
    # 9x9乘法表
    raw = 1
    while raw <= 9:
        lie = 1
        while lie <= raw:
            print("%dx%d=\t%d" % (raw, lie, raw * lie), end=" ")
            lie += 1
        print("")
        raw += 1


