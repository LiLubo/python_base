import random
# 从控制台输入要出的拳 石头（1）、剪刀（2）和布（3）
player = int(input("请输入您要出的拳 石头（1）、剪刀（2）和布（3）："))

# 电脑随机出拳
computer = random.randint(1, 3)

# 打印选择结果
print("玩家选择的拳是%d ,电脑出的拳是%d" % (player, computer))

# 比较胜负
if player == computer:
    print("平局")
elif ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家获胜")
else:
    print("电脑获胜")