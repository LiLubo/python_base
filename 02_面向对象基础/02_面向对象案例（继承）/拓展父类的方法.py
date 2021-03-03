# 李禄波
# 2021/1/27 12:40

class Animal:

    def eat(self):

        print("吃")

    def drink(self):

        print("喝")

    def run(self):

        print("跑")

    def sleep(self):

        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪汪汪。。。。")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞。。。。")

    def bark(self):

        # 调用父类中原有方法实现
        super().bark()

        # 使用类名调用父类原有方法
        Dog.bark(self)

        # 子类特有代码
        print("我是神犬，嗷呜。。。。")

        # 子类其他代码
        print("%&%^@^@")


# 定义对象
xiaotianquan = XiaoTianQuan()

xiaotianquan.bark()