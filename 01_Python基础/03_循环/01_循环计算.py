# case1: 计算 0~100 之间的数字的和
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print("0~100的和为%d" % sum)

# case2: 计算 0~100 之间的偶数之和
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print("0~100的偶数之和为%d" % sum)