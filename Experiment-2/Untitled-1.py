import math


def f(x): return math.pow(x//100, 3) + \
    math.pow(x//10 % 10, 3)+math.pow(x % 10, 3)


for x in range(100, 1000):
    if(f(x) == x):
        print(x)
