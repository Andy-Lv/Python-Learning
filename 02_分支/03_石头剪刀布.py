import random

player = int(input("请输入您出的："
                   "1、石头"
                   "2、剪刀"
                   "3、布"))
computer = random.randint(1, 4)  # 1<=computer<4
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("玩家胜出")
elif player == computer:
    print("平局")
else:
    print("电脑获胜")
