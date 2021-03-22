class Goods:
    def __init__(self, product, name, price, number) -> None:
        """构造方法

        Args:
            product (str): 商品编号
            name (str): 商品名称
            price (int): 单价
            number (int): 数量
        """
        self.__product = product  # 商品编号
        self.__name = name  # 商品名称
        self.__price = price  # 单价
        self.__number = number  # 数量

    def setPrice(self, price):
        """修改单价

        Args:
            price (int): 单价
        """
        self.__price = price

    def setNumber(self, number):
        """修改数量

        Args:
            number (int): 数量
        """
        self.__number = number

    def describe_Goods(self):
        """打印商品信息

        Returns:
            str: 商品信息
        """
        return self.__product+self.__name+self.__price+self.__number

    def number_Goods(self):
        """显示商品库存

        Returns:
            int: 数量
        """
        return self.__number

    def worth_Goods(self):
        """显示商品价值

        Returns:
            int: 单价
        """
        return self.__price


goods1 = Goods("001", "第一件商品", 10, 100)
goods2 = Goods("002", "第二件商品", 20, 200)
goods3 = Goods("003", "第三件商品", 30, 300)
total1 = goods1.number_Goods()+goods1.worth_Goods()
total2 = goods2.number_Goods()+goods2.worth_Goods()
total3 = goods3.number_Goods()+goods3.worth_Goods()
total = total1+total2+total3
print(total)
