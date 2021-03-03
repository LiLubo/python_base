def sum(num):
    """递归求和

    :param:num: 对 0~num 以内的数字递归求和
    :return:当前函数的和
    """
    # 递归出口
    if num == 1:
        return num

    # 递归调用
    num = sum(num - 1) + num

    # 返回值
    return num


result = sum(100)
print(result)