class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余面积：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("添加%s" % item.name)

        if item.area > self.free_area:
            print("%s的面积太大，无法添加", item.name)
            return

        self.item_list.append(item.name)
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("衣柜", 1)

my_home = House("三室一厅", 120)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
