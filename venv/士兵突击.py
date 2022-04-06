class Qiang:

    def __init__(self, name):

        self.name = name

        self.zdan = 0

    def add_bullet(self, Shuliang):

        self.zdan += Shuliang

    def shoot(self):
        if self.zdan <= 0:
            print("[%s]没有子弹" % self.name)
            return

        self.zdan -= 1

        print("[%s] 发出一颗子弹,剩余数量[%d]" % (self.name,  self.zdan))


ak1 = Qiang("wqw")
ak1.add_bullet(10)

n = 0
while ak1.zdan > 0:
    n += 1
    print(n)
    ak1.shoot()
print(n)
