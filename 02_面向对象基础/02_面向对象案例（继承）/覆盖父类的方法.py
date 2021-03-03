# 李禄波
# 2021/1/27 12:27

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
        print("\"我是神犬，嗷呜。。。。\"")


xiaotianquan = XiaoTianQuan()

# 在子类中重写了父类的方法，运行时只会调用子类的方法，不会调用父类的方法
xiaotianquan.bark()
