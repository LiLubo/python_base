#! /usr/bin/python3
import cards_tools

while True:

    # 显示功能菜单
    cards_tools.show_menu()

    # 提示
    action_int = int(input("请输入您想执行的操作："))
    print("您选择的操作是[%d]" % action_int)

    # 1，2，3 针对名片的操作
    if action_int in [1, 2, 3]:

        # 新建名片
        if action_int == 1:
            cards_tools.new_card()
        # 显示全部名片
        elif action_int == 2:
            cards_tools.show_all()
        # 查询名片
        else:
            cards_tools.search_card()
    # 0 退出系统
    elif action_int == 0:

        print("感谢您的使用，再见！")
        break
    # 输入超限
    else:
        print("输入超限，请正确输入！")