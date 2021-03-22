class KungFu:  # 定义一个父类
    def printKungfu(self):
        print('----功夫----')


class Panda:  # 定义另一个父类
    def eat(self):
        print('----吃竹子----')

    def __init__(self, color):
        self.color = color


class KungFuPanda(KungFu, Panda):  # 定义一个子类
    def eat(self):  # 重写父类的方法
        print('----吃包子----')

    def __init__(self, color, duan):  # 重写父类的方法
        super().__init__(color)  # 调用父类的init方法
        self.duan = duan  # 增加段位属性


Po = KungFuPanda('黑白', "六段")  # 定义功夫熊猫阿宝
Po.eat()
print("%s颜色的功夫熊猫阿宝的武功段位是%s" % (Po.color, Po.duan))
