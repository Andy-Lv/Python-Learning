def logging(flag):
    def func_out(func):
        def func_in(num1, num2):
            if flag == "+":
                print("加法")
            elif flag == "-":
                print("减法")
            result = func(num1, num2)
            return result

        return func_in

    return func_out


@logging('+')  # 1 logging("+")   2 @func_out  3 add=func_out(add)
def add(a, b):
    result = a + b
    return result


result = add(1, 2)
print(result)
