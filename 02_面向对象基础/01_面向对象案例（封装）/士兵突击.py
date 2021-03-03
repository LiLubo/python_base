# 李禄波
# 2021/1/26 20:16

# 士兵许三多有一把AK47
# 士兵可以开火
# 枪能够发射子弹
# 枪装填子弹（增加子弹的数量）

class Gun:

    def __init__(self, model):

        # 通过外界参数获取的属性
        self.model = model

        self.bullet_count = 0

    def add_bullet(self, count):

        # 添加子弹
        self.bullet_count += count

    def shoot(self):

        # 判断子弹数量是否足够
        if self.bullet_count == 0:

            print("【%s】没有子弹了...." % self.model)
            return

        # 发射子弹
        self.bullet_count -= 1

        # 提示信息
        print("【%s】突突突....【%d】" % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):

        # 定义姓名
        self.name = name

        # 定义枪（新兵没有枪）
        self.gun = None

    def fire(self):

        # 判断士兵是否有枪
        if self.gun is None:

            print("【%s】没有枪...." % self.name)
            return

        # 冲锋
        print("【%s】说：\"冲啊....\"" % self.name)

        # 装子弹
        self.gun.add_bullet(50)

        # 发射子弹
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")

# 创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47

xusanduo.fire()
