# 李禄波
# 2021/1/28 11:33

class Dog(object):

    @staticmethod
    def run():

        # 不访问实例属性/类属性
        print("小狗跑跑跑。。。。")


# 通过类名调用静态方法
Dog.run()