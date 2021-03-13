""" 生成一个由100以内能够被5整除的数组成的列表，然后将该列表的数字从大到小排序 """
l = list(range(5, 100, 5))
l.sort(reverse=True)
print(l)
