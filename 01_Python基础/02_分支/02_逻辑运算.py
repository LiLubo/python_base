var = "-" * 50
# case1: 定义一个整数变量 age， 编写代码判断年龄是否正确 0 <= age <= 20
print(var + "case1" + var)
age = int(input("请输入你的年龄："))

if 0 <= age <= 120:
    print("你的年龄是正确的")
else:
    print("你的年龄是错误的")

print("case1结束")

# case2:定义两个整数变量 python_score,c_score, 判断是否有成绩合格 （>=60）
print(var + "case2" + var)
python_score = int(input("请输入你的python分数："))
c_score = int(input("请输入你的c分数："))

if python_score >= 60 or c_score >= 60:
    print("你的成绩合格")
else:
    print("你的成绩不合格，请继续努力")

print("case2结束")

# case3:定义一个布尔型变量is_employee,编写代码判断是否是本公司员工，不是提示不允许入内
print(var + "case3" + var)
is_employee = False

if not is_employee:
    print("你不是本公司员工，禁止入内")