students_list = [
    {"name": "xiaoxue",
     "phone": "1234567",
     "gender": False,
     "weight": 100,
     "height": 170},
    {"name": "xiaodong",
     "phone": "7654321",
     "gender": True,
     "weight": 120,
     "height": 171}]

for student_dict in students_list:

    print(student_dict)
    if student_dict["name"] == "xiaohua":
        print("%s找到了" % student_dict["name"])
        break
else:
    print("%s 没有找到" % "xiaohua")

print("循环结束")