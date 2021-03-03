def say_hello():
    """打招呼"""
    print("Hello")
    print("Hello")
    print("Hello")


def sum_2_number(number1, number2):     # 带参函数
    """对两个数字进行求和,并将其结果作为返回值"""

    result = number1 + number2

    print("%d + %d = %d" % (number1, number2, result))

    say_hello()     # 函数的嵌套调用

    return result       # 返回值


def print_line(char, times):
    """单行多次打印指定字符"""
    print(char * times)


def print_lines(times_row, char, times_char):
    """打印多行分隔线

    :param times_row:分隔线打印的次数
    :param char: 分隔线打印的字符
    :param times_char: 单行分隔线字符重复的次数
    """
    i = times_row
    while i != 0:
        print_line(char, times_char)
        i -= 1


say_hello()

sum_result = sum_2_number(1, 2)     # 使用sum_result记录函数返回值
print(sum_result)

print_line("h", 20)     # 打印单行分隔线

print_lines(3, "*", 50)
