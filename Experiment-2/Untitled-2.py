import random

l = []


def RandomList(n, min=1, max=100):
    """生成随机数列表

    Args:
        n (int): 生成个数
        min (int, optional): 最小值. Defaults to 1.
        max (int, optional): 最大值. Defaults to 100.
    """
    for i in range(0, n):
        l.append(random.randint(min, max))


def PrimeNumber(x):
    """判断是否素数

    Args:
        x (int): [description]

    Returns:
        bool: 素数返回True,合数返回False
    """
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True


RandomList(100)
print(l)
sum = 0
for i in range(0, 100):
    result = PrimeNumber(l[i])
    if(result == True):
        print(l[i])
        sum += l[i]
print(sum)
