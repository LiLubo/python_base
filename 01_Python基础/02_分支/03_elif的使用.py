# 定义holiday_name字符串变量记录节日名称
holiday_name = input("请输入今天是什么节日：")

# 如果是 情人节， 买玫瑰/看电影
if holiday_name == "情人节":
    print("买玫瑰，看电影")

# 如果是 平安夜， 买苹果、吃大餐
elif holiday_name == "平安夜":
    print("买苹果，吃大餐")

# 如果是 生日， 买蛋糕
elif holiday_name == "生日":
    print("买蛋糕")

# 否则输出不再收录里
else:
    print("该节日暂未收录")