# 李禄波
# 2021/1/29 12:34

file = open("hello")

while True:
    text = file.readline()

    if not text:
        break

    print(text, end="")

file.close()
