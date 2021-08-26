class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 创建对象时new方法会被自动调用
        print("创建对象，分配空间")
        # 为对象分配空间
        instance = super().__new__(cls)  # 父类object的静态方法
        # 返回对象的引用
        return instance  # 否则python解释器得不到对象的地址

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()

print(player)
