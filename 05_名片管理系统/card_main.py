# ！/usr/bin/python3
import card_tools

while True:
    # 显示功能菜单
    card_tools.showmenu()

    choice = input("请选择操作:")
    print("您选择的操作是「%s」" % choice)

    if choice in ["1", "2", "3"]:
        # 如果在开发程序是不希望立即编写代码，
        # 可以用pass关键字来保证内部语法正确，
        # 程序运行时pass不会执行任何操作
        if choice == 1:
            # 新增名片
            card_tools.new_card()
        elif choice == 2:
            # 显示全部
            card_tools.show_all()
        else:
            # 查询名片
            card_tools.search_card()
    elif choice == 0:
        print("欢迎再次使用")
        break
    else:
        print("您输入的不正确，请重新输入")
