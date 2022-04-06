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

        print("[%s] 发出一颗子弹,剩余数量[%d]" % (self.name, self.zdan))


class Soldier:

    def __init__(self, name):
        self.name = name

        self.gun = None

    def fire(self):

        if self.gun == None:
            print("[%s]没枪" % self.name)

            return
        print("[%s]冲啊" % self.name)

        self.gun.add_bullet(50)

        self.gun.shoot()


ak = Qiang("wqw")

xusanduo = Soldier("许三多")
xusanduo.fire()
xusanduo.gun = ak
xusanduo.fire()

