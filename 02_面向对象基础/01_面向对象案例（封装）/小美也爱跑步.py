
# 小美体重 45.0 公斤
# 每跑步一次体重减少 0.5 公斤
# 每吃一次东西体重增加 1 公斤

class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "%s 的体重是 %.2f" % (self.name, self.weight)

    def run(self):

        print("%s 爱跑步" % self.name)

        self.weight -= 0.5

        print("%s 的体重是 %.2f" % (self.name, self.weight))

    def eat(self):

        print("%s 爱吃东西" % self.name)

        self.weight += 1

        print("%s 的体重是 %.2f" % (self.name, self.weight))


# 创建对象
xiaoming = Person("小明", 75.0)
xiaomei = Person("小美", 45.0)

print(xiaoming)
xiaoming.eat()
xiaoming.run()

print(xiaomei)
xiaomei.run()
xiaomei.eat()

print(xiaoming)
print(xiaomei)