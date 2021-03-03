# 李禄波
# 2021/1/28 12:49

class MusicPlayer(object):

    instance = None
    init_flag = False   # 记录是否执行过初始化方法

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否为空
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配内存空间
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 判断是否已经执行过了初始化方法
        if MusicPlayer.init_flag:
            return

        # 初始化动作
        print("初始化播放器")

        # 记录执行过初始化方法了
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
player2 = MusicPlayer()

print(player1)
print(player2)


