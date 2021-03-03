# 李禄波
# 2021/1/28 18:50

from distutils.core import setup

setup(name="包",     # 包名
      version="1.0",    # 版本
      description="发送和接收信息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="Lubo",    # 作者
      author_email="1611217783@qq.com",     # 作者邮箱
      url="www.lubo.com",   # 主页
      py_modules=["包.send_message",     # 包中的模块
                  "包.receive_message"])
