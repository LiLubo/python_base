
# 房子（House）有户型，总面积和家具名称列表
# 家具（HouseItem）有名字和占地面积，其中
# 席梦思（bed）占地 4 平米
# 衣柜（chest）占地 2 平米
# 餐桌（table）占地 1.5 平米
# 将上述三件家具添加到房子中
# 打印房子时要求输出：户型，总面积，剩余面积和家具名称列表

class HouseItem:

    def __init__(self, name, area):
        """家具初始化方法

        :param name: 家具名
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] 占地 %.2f 平米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        # 通过形参确定的属性
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具列表
        self.item_list = []

    def __str__(self):

        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):

        print("要添加 %s" % item)
        # 判断家具面积是否能够添加
        if item.area > self.free_area:

            print("%s 的面积太大了，无法添加" % item.name)
            return

        # 将家具的名称添加到房子的家具列表
        self.item_list.append(item.name)

        # 计算剩余面积
        self.free_area -= item.area


# 创建家具对象
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 200)
table = HouseItem("餐桌", 1.5)

print("=" * 50)
print(bed)
print(chest)
print(table)

# 创建房子对象
my_house = House("两室一厅", 120)

# 添加家具
print("=" * 50)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print("=" * 50)
print(my_house)
