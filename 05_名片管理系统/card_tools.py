card_list = []


def showmenu():  # 显示菜单
    print("#" * 50)
    print("欢迎使用名片管理系统  v 1.0")
    print("")
    print("1、新增名片")
    print("")
    print("2、显示全部")
    print("")
    print("3、查询名片")
    print("#" * 50)


def new_card():
    """新增名片"""
    print("#" * 25)
    name_str = input("please input the name")
    phone_str = input("please input the phone number")
    qq_str = input("please input the qq number")
    email_str = input("please input the email")

    card = {"name": name_str,
            "phone": phone_str,
            "qq": qq_str,
            "email": email_str}

    card_list.append(card)

    print("Add the card success!!")


def show_all():
    """显示所有名片"""
    print("#" * 25)

    if len(card_list) != 0:
        # 打印表头
        for name in ["姓名", "电话", "QQ", "邮箱"]:
            print(name, end="\t\t")
        print("")

        print("=" * 25)

        for card_dict in card_list:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))
    else:
        print("当前没有记录")
        return


def search_card():
    """查询名片"""
    print("#" * 25)

    find_name = input("please input you finding name")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("finding success!!")

            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")

            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))

            deal_card(card_dict)

            break
    else:
        print("未找到该名片")


def deal_card(find_dict):
    """针对查询到的人进行操作"""
    action_str = input("请输入执行的操作 1、修改  2、删除  0、返回")

    if action_str == "1":
        find_dict["name"] = input_Card_info(find_dict["name"], "姓名[回车不修改]:")
        find_dict["phone"] = input_Card_info(find_dict["phone"], "电话[回车不修改]:")
        find_dict["qq"] = input_Card_info(find_dict["qq"], "QQ[回车不修改]:")
        find_dict["email"] = input_Card_info(find_dict["email"], "邮件[回车不修改]:")
        print("修改成功")

    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除成功")

    elif action_str == "0":
        return
    else:
        print("输入错误")


def input_Card_info(dict_value, tip_message):
    """修改名片信息，实现回车之后不修改
    用户输入了内容就返回内容，否则就返回字典中原有的值"""
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
