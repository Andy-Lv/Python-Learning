# 私有属性和方法可以在名称前面增加"__"
class Woman:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s的年龄是 %d" % (self.name, self.__age))


xiaofang = Woman("小芳")

#print(xiaofang.__age)  # 会报错，因为访问不到私有属性
print(xiaofang._Woman__age)
xiaofang._Woman__secret()
