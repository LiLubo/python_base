# 李禄波
# 2021/1/28 12:37

# 让类创建的对象，在系统中只有唯一的一个实例
# 定义一个类属性，初始值是 None,用于记录单例对象的引用
# 重写 __new__ 方法
# 如果类属性 is None，调用父类方法分配空间，并在类属性中记录结果
# 返回类属性中记录的对象引用

class MusicPlayer(object):

    instance = None

    def __new__(cls, *args, **kwargs):

        # 判断类属性是否为空
        if cls.instance is None:

            # 调用父类方法，为第一个对象分配内存空间
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance


player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1)
print(player2)

