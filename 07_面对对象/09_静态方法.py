class Dog(object):
    @staticmethod
    def run():
        print("小狗要跑")


Dog.run()  # 静态方法调用的时候不需要对象，可以直接用类名调用
