def print_info(name, gender=True):  # 缺省参数必须在参数的末尾
    gender_text = "man"
    if not gender:
        gender_text = "woman"

    print("%s is %s" % (name, gender_text))


print("xiaoming")
print("xiaomei", False)
