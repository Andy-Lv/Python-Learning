code = input("Please Input Your Code ")  # input函数输入的任何东西都是一个字符串

# test
price_str = input("please input the price of apple ")

weight_str = input("please input the weight of apple ")

money = float(price_str) * float(weight_str)

print("the cost of apple is %d" % money)

print("the cost of apple is %06d" % money)  # "06d"表示6位数输出，没有的位用0填充

print("苹果单价 %.02f 元／斤，购买 %.02f 斤，需要支付 %.02f 元" % (float(price_str), float(weight_str), money))
print("数据比例是 %.02f%%" % (0.25 * 100))  # "%%"表示输出一个%
