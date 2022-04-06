class Person:

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def eat(self):
        self.weight = self.weight + 5

    def run(self):
        self.weight = self.weight - 3

    def __str__(self):
        return "我是 %s 体重 %.2f 公斤 " % (self.name , self.weight)


p = Person("小明",75)
print(p)

p2 = Person("小红",75)
p2.eat()
p2.run()
print(p2)
print(p)