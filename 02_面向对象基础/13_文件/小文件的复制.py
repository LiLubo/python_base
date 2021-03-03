# 李禄波
# 2021/1/29 12:40

# 打开文件
read_file = open("hello")
write_file = open("hello[副本]", "w")

# 读写操作
text = read_file.read()
write_file.write(text)

# 关闭文件
read_file.close()
write_file.close()

