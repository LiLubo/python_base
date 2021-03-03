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