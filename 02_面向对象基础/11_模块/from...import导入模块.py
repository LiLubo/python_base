# 李禄波
# 2021/1/28 16:36

from test_model1 import Dog
from test_model2 import say_hello as say_hello2  # 起别名
from test_model1 import say_hello  # 导入不同模块的同名函数， 后导入的会覆盖先导入的

dog = Dog()
say_hello()     # test_model1 的函数
say_hello2()    # test_model2 的函数

print(dog)
