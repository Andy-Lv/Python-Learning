class Person:
    def __init__(self, name, weight):  # 初始化
        self.name = name
        self.weight = weight

    def __str__(self):  # 可以在打印这个类的时候输出下面return的语句
        return "我的名字叫做%s,体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s love running" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s love eating" % self.name)
        self.weight += 1


andy = Person("andy", 75.0)
andy.run()
andy.eat()
print(andy)
