# 记录所有名片字典
cards_list = []


# 功能菜单
def show_menu():

    """显示功能菜单"""
    print("-" * 50)
    print("欢迎使用[名片管理系统V1.0]")
    print("")
    print("1.新增名片")
    print("2.显示全部名片")
    print("3.搜索名片")
    print("0.退出系统")
    print("-" * 50)


def new_card():

    """新增名片"""
    print("*" * 50)
    print("新增名片")

    # 1.名片信息的输入
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_number_str = input("请输入QQ号码：")
    email_str = input("请输入邮箱:")

    # 2.建立字典名片
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq_number": qq_number_str,
                 "email": email_str}

    # 3.将已建立的字典添加到卡片列表中
    cards_list.append(card_dict)

    # 4.提示添加成功
    print("%s添加成功" % card_dict["name"])


def show_all():

    """显示所有名片"""
    print("*" * 50)
    print("显示所有名片")

    # 判断是否存在名片
    if len(cards_list) == 0:

        print("无名片记录")
        return

    # 打印表头
    for info in ["姓名", "电话", "QQ号码", "邮箱"]:

        print(info, end="\t\t")
    print("")

    # 打印分隔线
    print("-" * 50)

    # 打印名片
    for card_dict in cards_list:

        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq_number"],
                                        card_dict["email"]))


def search_card():

    """搜索名片"""
    print("*" * 50)
    print("搜索所有名片")

    search_name = input("请输入你想要搜索的姓名：")

    for card_dict in cards_list:

        if card_dict["name"] == search_name:

            print("姓名\t\t电话\t\tQQ号码\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq_number"],
                                            card_dict["email"]))
            # 修改和删除
            deal_card(card_dict)
            break

    else:
        print("没找到%s" % search_name)


def deal_card(search_dict):
    """处理名片信息

    :param search_dict: 要处理的名片
    """
    print(search_dict)

    action_str = int(input("请输入你想要进行的操作:  1:修改 2：删除 0返回上级菜单"))

    if action_str == 1:

        search_dict["name"] = input_card_info(search_dict["name"], "请输入姓名：[回车不修改]")
        search_dict["phone"] = input_card_info(search_dict["phone"], "请输入电话号码：[回车不修改]")
        search_dict["qq_number"] = input_card_info(search_dict["qq_number"], "请输入QQ号码:[回车不修改]")
        search_dict["email"] = input_card_info(search_dict["email"], "请输入email:[回车不修改]")

        print("名片修改成功！")

    elif action_str == 2:

        cards_list.remove(search_dict)

        print("名片删除成功！")

    else:

        print("返回上级菜单")
        return


def input_card_info(dict_value, tip_message):
    """修改名片

    :param dict_value: 名片原有的信息
    :param tip_message: 提示信息
    :return:
    """
    # 1.提示用户输入信息
    result_str = input(tip_message)

    # 2.针对用户输入的信息进行判断，如果用户进行了输入，则替换原有内容
    if len(result_str) > 0:
        return result_str

    # 3.如果用户没有输入内容，则不修改原有内容
    else:
        return dict_value