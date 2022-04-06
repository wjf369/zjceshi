class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return ("户型: %s\n总面积: %.2f[剩余： %.2f] 家具 %s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加 %s" % item)

        # 判断家具的面积
        if item.area > self.free_area:
            print("%s 太大不能添加" % item.name)

            return

        # 将家具的名称加入到列表
        self.item_list.append(item.name)

        # 计算剩余面积
        self.free_area -= item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 300)
# print(bed, chest, table)

# 创建房子
house = House("三居室", 100)
# print(house)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)
for i in house.item_list:
    print(i)
