# 字典是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序与定义的顺序不一致
ali_dict = {"name": "ali",
            "age": 19,
            "gender": True
            }

var = "-" * 50

# 取值(在取值时，若指定的键不存在，则会报错)
print(var + "取值" + var)
print(ali_dict["name"], ali_dict["age"], ali_dict["gender"])

# 增加元素（key不存在则新增）
print(var + "增加元素" + var)
ali_dict["weight"] = 120
print(ali_dict)

# 修改元素（key已存在则修改）
print(var + "修改元素" + var)
ali_dict["name"] = "阿李"
print(ali_dict)

# 删除 pop    (key存在则删除，key不存在则报错)
print(var + "删除元素" + var)
ali_dict.pop("age")
print(ali_dict)

# 统计键值对数量
print(var + "统计键值对数量" + var)
print(len(ali_dict))

# 合并字典(如果被合并的字典中有与原字典相同的键，则会覆盖原字典)
print(var + "合并字典" + var)
temp_dict = {"height": 170}
ali_dict.update(temp_dict)
print(ali_dict)

# 清空字典
print(var + "清空字典" + var)
ali_dict.clear()
print(ali_dict)

# 迭代遍历
print(var + "迭代遍历" + var)
ali_dict = {"name": "ali",
            "age": 19,
            "gender": True
            }

for key_ali_dict in ali_dict:

    print("%s: %s" % (key_ali_dict, ali_dict[key_ali_dict]))

# 字典与列表的共同应用
print(var + "字典与列表的共同应用" + var)
card_list = [{"name": "ali",
              "qq": "123456",
              "phone": "12456"},
             {"name": "azi",
              "qq": "123456",
              "phone": "123456"}]

for card_info in card_list:

    print(card_info)