# 李禄波
# 2021/1/28 14:49

# 提示用户输入一个整数
# 使用 8 除以用户输入的整数并且输出

try:
    num = int(input("请输入一个整数:"))
    print("8 / %d = %.2f" % (num, 8 / num))

# 对除数为 0 进行处理
except (ZeroDivisionError, ValueError):
    print("请不要输入 0")

# 对输入非整数进行处理
except ValueError:
    print("请输入正确的整数")

# 对未知错误进行处理
except Exception as result:
    print("未知错误 %s" % result)

# 所尝试执行的代码没有出现异常才会执行的语法
else:
    print("我是 else,我执行说明你所尝试执行的代码没有出现异常")

# 无论是否出现异常都会执行的代码
finally:
    print("我是 finally,无论是否出现异常我都会执行")

