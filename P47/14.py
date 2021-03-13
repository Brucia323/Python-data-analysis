""" 已知：列表 lst1=[1,2,3,4,5,6]，lst2=[“a”，“b”，“c”，“d”]。 要求：以lst1的元素为key，以lst2的元素为value建立一个字典，并打印输出 """
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = ["a", "b", "c", "d"]
d = {}
for i in range(len(lst2)):
    d1 = "{}".format(lst1[i])
    d2 = "{}".format(lst2[i])
    d[d1] = d2
print(d)
