# 李禄波
# 2021/1/29 12:06

file = open("hello")

print(file.read())

# 再次执行read因为文件指针已经到了末尾，读取不到文件
print(file.read())

file.close()
