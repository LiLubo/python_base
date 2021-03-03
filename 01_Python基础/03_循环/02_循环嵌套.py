# case1:在控制台连续输出五行 * 号，每行的星号依次递增
# *
# **
# ***
# ****
# *****
var = "-" * 50
print(var + "case1" + var)
i = 0
while i < 5:
    i += 1
    j = 0
    while j < i:
        print("*", end="")
        j += 1
    print("")

# case2:打印九九乘法表
print(var + "case2" + var)
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d\t" % (j, i, i*j), end=" ")
        j += 1
    print("")
    i += 1