class Goods:
    __number_sell = 0

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

    def sell(self, sellNumber):
        """卖出商品

        Args:
            sellNumber (int): 卖出数量
        """
        self.__number_sell += sellNumber
        self.__number -= sellNumber

    def getNumber_Sell(self):
        """获取卖出数量

        Returns:
            int: [description]
        """
        return self.__number_sell


goods = Goods("001", "商品", 10, 100)
goods.sell(50)
print("有"+(str)(goods.number_Goods()+goods.getNumber_Sell())+"件商品卖出了" +
      (str)(goods.getNumber_Sell()) + "件，还剩下"+(str)(goods.number_Goods())+"件商品")
