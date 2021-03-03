# 李禄波
# 2021/1/27 17:00

class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的属性
    count = 0

    def __init__(self, name):

        self.name = name

        # 每定义一个实例对象，count加1
        Tool.count += 1


# 创建工具类对象
tool1 = Tool("扳手")

print(Tool.count)
print(tool1.count)

tool2 = Tool("小刀")

print(Tool.count)
print(tool1.count)
print(tool2.count)

# 当对 对象名.类属性 进行赋值时，会为该对象创建一个属性，而不会影响到类属性
tool2.count = 10
print(tool2.count)
print(Tool.count)
