# 李禄波
# 2021/1/28 15:19

# 定义函数 demo1() 提示用户输入一个整数并将其作为返回值
# 定义函数 demo2() 调用 demo1()
# 在主程序中调用 demo2()

def demo1():

    return 8 / int(input("请输入一个整数："))


def demo2():
    return demo1()


while True:
    try:
        print("8 / num = %.2f" % demo2())

    except ZeroDivisionError:
        print("请输入非零的整数！")

    except ValueError:
        print("请输入正确的整数！")

    else:
        print("你的输入正确！！！！")
        break
