# 李禄波
# 2021/1/28 11:39

# 设计 Game 类
# 属性：
# 1.类属性 top_score 记录游戏的最高分
# 2.实例属性 player_name 记录当前玩家姓名
# 方法：
# 1.静态方法 show_help 显示游戏帮助信息
# 2.类方法 show_top_score 显示游戏最高分
# 3.实例方法 start_game 开始当前玩家的游戏
# 主程序步骤
# 1.查看帮助信息
# 2.查看历史最高得分
# 3.创建游戏对象，开始游戏

class Game(object):

    # 类属性
    top_score = 0

    # 类方法
    @classmethod
    def show_top_score(cls):

        print("您的游戏最高分是 %d" % cls.top_score)

    # 静态方法
    @staticmethod
    def show_help():

        print("这是帮助信息")

    # 初始化方法
    def __init__(self, player_name):

        self.player_name = player_name

    # 实例方法
    def star_game(self):

        print("%s 你好！游戏开始了。。。。" % self.player_name)
        Game.top_score = 100


# 查看帮助信息
Game.show_help()

# 查看历史最高得分
Game.show_top_score()

# 创建玩家对象
player = Game("小明")

# 开始游戏
player.star_game()

Game.show_top_score()
