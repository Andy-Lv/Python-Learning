age = int(input("请输入年龄"))

# else if == elif
if age >= 0 and age <= 120:  # 相当于 0 <= age <= 120
    print("年龄正确")
    if age >= 60 or age <= 18:
        print("你还不适合工作")
else:
    print("年龄输入错误")

is_employee = True

if not is_employee:
    print("非公司人员不得入内")

# Tab键统一添加缩进
# shift+Tab键统一减小缩进
