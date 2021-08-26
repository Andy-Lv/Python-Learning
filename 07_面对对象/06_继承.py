class Animal:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("bark wang! wang!")


class XiaoTianQuan(Dog):
    def bark(self):
        print("bark aowuaowu")

        super().bark()  # 利用super来调用父类中被重写的代码
        Dog.bark(self)  # 利用父类名来调用父类中的代码，必须加self,且不能使用自己的类名递归，会无限循环
