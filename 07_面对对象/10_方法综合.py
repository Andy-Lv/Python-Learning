class Game(object):
    # 历史最高分
    top_score = 0  # 类属性

    def __init__(self, player_name):
        self.player_name = player_name  # 实例属性，实例才能访问的属性

    @staticmethod  # 静态方法
    def show_help():
        print("帮助信息:让僵尸进入大门")

    @classmethod  # 类方法
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    def start_game(self):  # 实例方法
        print("%s开始游戏" % self.player_name)


# 查看游戏的帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
game=Game("xiaoming")
game.start_game()