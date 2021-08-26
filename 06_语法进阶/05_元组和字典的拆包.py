def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_num = (1, 2, 3)
gl_dict = {"name": "xiaoming", "age": 18}

demo(gl_num, gl_dict)  # 两个参数都传入了元组中

demo(*gl_num, **gl_dict)  # 前一个参数在元组中，后一个参数在字典中
