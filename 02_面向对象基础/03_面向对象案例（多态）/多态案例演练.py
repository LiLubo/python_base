# 李禄波
# 2021/1/27 16:03

class Dog(object):

    def __init__(self, name):

        self.name = name

    def game(self):

        print("我们是【%s】，我们在简单的玩耍。。。。" % self.name)


class XiaoTian(Dog):

    def game(self):

        print("我们是【%s】，我们在天上玩耍。。。。" % self.name)


class Person(object):

    def __init__(self, name):

        self.name = name

    def game_with_dog(self, dog):

        print("我是【%s】,我正在和【%s】玩耍" % (self.name, dog.name))
        dog.game()


# 定义普通狗
normal_dog = Dog("土狗")

# 定义哮天狗
god_dog = XiaoTian("哮天狗")

# 定义人对象
huluwa = Person("葫芦娃")

huluwa.game_with_dog(normal_dog)
huluwa.game_with_dog(god_dog)





