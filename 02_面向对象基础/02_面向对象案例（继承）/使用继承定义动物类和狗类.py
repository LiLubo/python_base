# 李禄波
# 2021/1/27 12:09

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


class Cat(Animal):

    def catch(self):
        print("我会抓老鼠")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞。。。。")


# 定义对象
wangcai = XiaoTianQuan()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
wangcai.fly()
