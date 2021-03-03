# 李禄波
# 2021/1/29 13:28

# 不要用eval()函数直接转换input的结果，因为eval同样可以通过os模块执行文件系统的操作
# 如删除文件，修改文件等，风险太大
# print(eval(input("请输入一个表达式")))

info = input("请输入一个表达式")

print(eval(info))
