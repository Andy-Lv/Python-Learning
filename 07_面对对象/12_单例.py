class MusicPlayer(object):
    instance = None  # 记录第一个被创建对象的引用
    init_flag = False  # 记录是否执行过初始化动作

    def __new__(cls, *args, **kwargs):  # 实现所有的实例对象所运用的是一个内存地址
        # 判断类属性是不是空对象
        if cls.instance is None:
            # 调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回类属性保存的引用
        return cls.instance

    def __init__(self):
        # 判断是否执行过初始化
        if MusicPlayer.init_flag:
            return

        # 如果没有执行过，再执行初始化动作
        print("初始化播放器")
        # 修改类属性标记
        MusicPlayer.init_flag = True


player = MusicPlayer()
print(player)

player1 = MusicPlayer()
print(player1)
