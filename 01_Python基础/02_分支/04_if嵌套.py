# 定义bool型变量 has_ticket 表示是否有车票
has_ticket = True

# 定义整形变量 knife_length 表示刀的长度
knife_length = 30

# 检查是否有车票
if has_ticket:
    print("您已进入安检阶段")
    # 判断刀的长度
    if knife_length >= 20:
        print("您所携带的刀具为%dcm，安检不通过" % knife_length)
    # 安检通过
    else:
        print("您所携带的刀具在安全范围内，安检通过")
# 没票，提示
else:
    print("你还未购买车票，请先购票")