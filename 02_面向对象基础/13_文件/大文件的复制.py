# 李禄波
# 2021/1/29 12:43

read_file = open("hello")
write_file = open("hello[big_副本]", "w")

while True:
    text = read_file.readline()

    if not text:
        break

    write_file.write(text)

read_file.close()
write_file.close()
