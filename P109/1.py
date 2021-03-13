""" 在0~9之间随机选择1个整数，操作100次，统计共有几种数字，并用字典的方式输出每个数字的出现次数，键是出现的整数，值是出现的次数。 """
import random
num_list = []
for i in range(0, 100):
    number = random.randint(0, 9)
    num_list.append(number)
result = {}
for num in num_list:
    if num in result.keys():
        result[num] += 1
    else:
        result[num] = 1
print(result)
