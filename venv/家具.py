class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 占地 %.2f" % (self.name, self.area)


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 3)
print(bed, chest, table)

