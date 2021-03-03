fruit_list = ["apple", "banana", "pears", "grapes"]
var = "_" * 50

# 取值：已知索引获取数据(超出索引范围会报错)
print(var + "取值" + var)
print(fruit_list[1])

# 取索引：已知数据获取索引(数据在列表中不存在会报错)
print(var + "取索引" + var)
print(fruit_list.index("pears"))


# 修改指定位置的数据（超出索引范围会报错）
print(var + "修改指定位置的数据" + var)
fruit_list[1] = "apples"
print(fruit_list)

# 增加数据 append，insert, extend
print(var + "增加数据" + var)
fruit_list.append("peach")  # append可在列表末尾追加数据
print(fruit_list)
fruit_list.insert(1, "orange")  # insert可在列表的指定位置插入数据
print(fruit_list)
temp_list = ["plum", "grapefruit"]  # 临时列表
fruit_list.extend(temp_list)    # extend可将列指定表中的所有数据追加到当前列表的末尾
print(fruit_list)

# 删除数据 del, remove，clear，pop
print(var + "删除数据" + var)
del fruit_list[0]   # del关键字可以删除指定位置的元素（del本质上是将变量从内存中删除）
print(fruit_list)
fruit_list.remove("plum")   # remove从列表中删除第一次出现的指定数据
print(fruit_list)
fruit_list.pop()    # pop不带参数则删除列表中的末尾元素
print(fruit_list)
fruit_list.pop(1)     # pop 带参则删除指定位置的数据
print(fruit_list)
fruit_list.clear()  # clear清空列表中的所有元素
print(fruit_list)

# 列表统计 len(),count
fruit_list = ["apple", "banana", "pears", "grapes", "apple"]
print(var + "列表统计" + var)
print("列表中的元素个数为%d" % len(fruit_list))  # len（）用于获取列表长度
print("apple出现了%d次" % fruit_list.count("apple"))  # count用于获取某个数据在列表中出现的个数

# 列表排序 .sort(),.sort(reverse==True),.reverse
print(var + "列表排序" + var)
number_list = [9, 1, 4, 2, 22, 1]
print(number_list)
number_list.sort()  # .sort()升序
print(number_list)
number_list.sort(reverse=True)  # .sort(reverse=True)降序
print(number_list)
number_list.reverse()  # .reverse()翻转/逆序
print(number_list)

# 循环遍历 for...in...
for fruit_name in fruit_list:
    print("水果的名称是：%s" % fruit_name)