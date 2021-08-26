class Tool(object):
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量%d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("锯子")

# 调用类方法
Tool.show_tool_count()
