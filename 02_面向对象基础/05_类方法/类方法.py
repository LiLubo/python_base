# 李禄波
# 2021/1/27 19:15

# 定义一个工具类
# 每件工具都有自己的 name
# 在类中封装一个 show_tool_count 的类方法，输出使用当前这个类创建的对象个数

class Tool(object):

    # 定义类属性
    tool_count = 0

    def __init__(self, name):

        self.name = name

        # 记录工具数量
        Tool.tool_count += 1

    # 定义类方法
    @classmethod
    def show_tool_count(cls):

        print("工具对象的数量 %d " % cls.tool_count)


# 定义类对象
tool1 = Tool("扳手")

Tool.show_tool_count()

tool2 = Tool("斧头")

Tool.show_tool_count()
