import random


class Play:
    def __init__(self, nickname) -> None:
        """构造方法

        Args:
            nickname (str): 昵称
        """
        self.__nickname = nickname  # 昵称
        self.__score = 0  # 分数

    def punches(self):
        pass

    def win(self):
        """获胜
        """
        self.__score += 1

    def printScore(self):
        """显示分数

        Returns:
            str: [description]
        """
        return self.__nickname+"："+str(self.__score)+"分"


class Computer(Play):
    def __init__(self) -> None:
        """构造方法
        """
        super().__init__("computer")

    def punches(self):
        """出拳

        Returns:
            int: [description]
        """
        return random.randint(0, 2)

    def win(self):
        """获胜
        """
        super().win()

    def printScore(self):
        """显示分数

        Returns:
            str: [description]
        """
        return super().printScore()


class Person(Play):
    def __init__(self, nickname) -> None:
        """构造方法

        Args:
            nickname (str): 昵称
        """
        super().__init__(nickname)

    def punches(self):
        """出拳
        """
        super().punches()

    def win(self):
        """获胜
        """
        super().win()

    def printScore(self):
        """显示分数

        Returns:
            str: [description]
        """
        return super().printScore()


class Game:
    def __init__(self, nickname) -> None:
        """构造方法

        Args:
            nickname (str): 昵称
        """
        self.__person = Person(nickname)
        self.__computer = Computer()

    def determine(self, gesture):
        """判定

        Args:
            gesture (int): 手势

        Returns:
            str: [description]
        """
        __computer = self.__computer.punches()
        __person = gesture
        if(__computer == __person):
            return "平局"
        elif(__computer == 0):
            if(__person == 1):
                self.__person.win()
                return "你赢了"
            else:
                self.__computer.win()
                return "你输了"
        elif(__computer == 1):
            if(__person == 0):
                self.__computer.win()
                return "你输了"
            else:
                self.__person.win()
                return "你赢了"
        else:
            if(__person == 0):
                self.__person.win()
                return "你赢了"
            else:
                self.__computer.win()
                return "你输了"

    def printScore(self):
        """显示分数

        Returns:
            str: [description]
        """
        return self.__person.printScore()+" "+self.__computer.printScore()


print("游戏规则：0代表石头，1代表布，2代表剪刀，输入其他数字退出")
nickname = input("请输入昵称：")
game = Game(nickname)
print("游戏开始")
counter = 0
while 1:
    gesture = int(input("请出拳："))
    if(gesture < 0 or gesture > 2):
        print(game.printScore())
        print("你一共玩了"+str(counter)+"次")
        break
    print(game.determine(gesture))
    counter += 1
