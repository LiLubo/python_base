# 李禄波
# 2021/1/28 12:28

class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 1.创建对象，new方法自动调用
        print("创建对象，new方法调用分配空间")

        # 2.为对象分配空间
        instance = super().__new__(cls)

        # 3.返回对象的引用
        return instance

    def __init__(self):

        print("音乐播放器初始化完成")


# 创建播放器对象
player = MusicPlayer()

print(player)
