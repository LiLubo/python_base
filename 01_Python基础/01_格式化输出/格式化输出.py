# 定义字符串变量 name ， 输出 我叫小明，请多多关照！
var = "-" * 50
print(var + "cast1" + var)
name = "小明"
print("我叫%s，请多多关照！" % name)

# 定义整数变量 student_no, 输出 我的学号是000001
print(var + "case2" + var)
student_no = "1"
print("我的学号是%06d")

# 定义小数 price, weight, money, 输出 苹果单价 9.00 元/斤，购买了 5.00 斤，需要支付 45 元
print(var + "case3" + var)
price = int(input("请输入单价："))
weight = int(input("请输入重量："))
money = price * weight
print("苹果单价%.2f元/斤，购买了%.2f斤，需要支付%.0f元" % (price, weight, money))

# 定义一个小数scale，输出 数据比例是10%
print(var + "case4" + var)
scale = 20
print("数据比例是%.2f%%" % (scale / 2))