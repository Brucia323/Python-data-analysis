""" 已知两个列表：citys = [“suzhou”，“shanghai”，“hangzhou”，“nanjing”]，codes = [“0512”，“021”，“0571”，“025”]。 要求：创建一个字典，以citys中的元素为key，以codes中的元素为value。 """
citys = ["suzhou", "shanghai", "hangzhou", "nanjing"]
codes = ["0512", "021", "0517", "025"]
d = {}
for i in range(len(citys)):
    d1 = "{}".format(citys[i])
    d2 = "{}".format(codes[i])
    d[d1] = d2
print(d)
