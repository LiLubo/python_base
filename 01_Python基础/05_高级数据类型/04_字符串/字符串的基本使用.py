var = "_" * 50
# 使用单引号和双引号共同定义字符串
print(var + "基础方法" + var)
str1 = "I say 'hello python' "
str2 = 'I sat "hello python" '

print(str1)
print(str2)

# 取值
print(str1[13])

# 循环遍历
for char in str1:

    print(char)

# 统计字符串长度
print(len(str1))

# 统计小字符串出现的次数
print(str1.count("llo"))

# 获取子串在主串中第一次出现时的索引(若字串不存在则报错)
print(str1.index("llo"))

# 字符串的查找和替换
print(var + "字符串的查找和替换" + var)
hello_str = "hello word"

# 判断主串是否以指定字符串开始
print(hello_str.startswith("hello"))

# 判断主串是否以指定字符串结束
print(hello_str.endswith("word"))

# 在主串中查找子串（字串不存在，返回-1）
print(hello_str.find("abc"))

# 替换字符串(返回的十一个替换后的字符串，原字符串并不会被修改)
print(hello_str.replace("word", "Python"))
print(hello_str)

print(var + "文本对齐" + var)
# 居中，左，右对齐
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:

    print("|%s| |%s| |%s|" % (poem_str.rjust(10, "　"),
                              poem_str.center(10, "　"),
                              poem_str.ljust(10, "　")))

# 去除空白字符
print(var + "去除空白字符" + var)
# 顺序并居中对齐输出以下内容
poem = ["\t\n登鹳雀楼",
        "王之涣\t\t",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:

    # 先使用strip方法去除字符串中的空白字符，再居中输出
    print("|%s|" % poem_str.strip().center(10, "　"))

# 字符串的拆分和连接
print(var + "字符串的拆分和连接" + var)
poem = "\t\n登鹳雀楼 \t 王之涣\t\t 白日依山尽 黄河入海流  欲穷千里目\t 更上一层楼"

# 拆分字符串(将字符串中的所有空白字符全部去掉)
poem_list = poem.split()
print(poem_list)

# 连接字符串
print("\n".join(poem_list))

# 字符串的切片
print(var + "字符串的切片" + var)
num_str = "0123456789"

# 截取 2~5
print(num_str[2: 6])

# 截取 2~末尾
print(num_str[2:])

# 截取 开始~5
print(num_str[: 6])

# 截取 完整字符串
print(num_str[:])

# 从开始位置，每隔一个位置截取一个字符
print(num_str[::2])

# 从 1开始 每隔一位取一个字符
print(num_str[1::2])

# 截取从 2到末尾-1的字符
print(num_str[2: -1])

# 截取 字符串末尾的两位字符
print(num_str[-2:])

# 获取字符串的逆序
print(num_str[-1: 0: -1])





