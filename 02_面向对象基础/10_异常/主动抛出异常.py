# 李禄波
# 2021/1/28 15:35

# 定义 input_password() 函数，提示用户输入密码
# 如果用户输入的密码长度小于 8位 ，抛出异常
# 如果用户输入的密码长度不小于 8位，返回输入的密码

def input_password():

    # 提示用户输入密码
    pwd = input("请输入你的密码：")

    # 密码长度小于 8
    if len(pwd) < 8:
        # 创建异常对象,并抛出
        raise Exception("密码长度不够")

    return pwd


try:
    print(input_password())

except Exception as result:
    print(result)
