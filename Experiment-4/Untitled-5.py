import numpy as np
from numpy.core.fromnumeric import std
from numpy.lib.function_base import median
import matplotlib.pyplot as plt


datas3 = np.loadtxt('iris.csv', delimiter=",",
                    skiprows=1, usecols=[0, 1, 2, 3])
datas4 = np.loadtxt('iris.csv', delimiter=",", skiprows=1,
                    dtype=str, encoding='UTF-8', usecols=[4])

datas3 = datas3.T  # 转置
sepal_length = datas3[0]  # 花萼长度，单位cm
sepal_width = datas3[1]  # 花萼宽度，单位cm
petal_length = datas3[2]  # 花瓣长度，单位cm
petal_width = datas3[3]  # 花瓣宽度，单位cm
species = datas4  # 种类

""" 均值 """
sepal_avglength = np.average(sepal_length)
sepal_avgwidth = np.average(sepal_width)
petal_avglength = np.average(petal_length)
petal_avgwidth = np.average(petal_width)
print("花萼长度均值："+sepal_avglength+" 花萼宽度均值："+sepal_avgwidth +
      " 花瓣长度均值："+petal_avglength+" 花瓣宽度均值："+petal_avgwidth)
""" 标准差 """
sepal_stdlength = std(sepal_length)
sepal_stdwidth = std(sepal_width)
petal_stdlength = std(petal_length)
petal_stdwidth = std(petal_width)
print("花萼长度标准差："+sepal_stdlength+" 花萼宽度标准差："+sepal_stdwidth +
      " 花瓣长度标准差："+petal_stdlength+" 花瓣宽度标准差："+petal_stdwidth)
""" 最大值 """
sepal_maxlength = max(sepal_length)
sepal_maxwidth = max(sepal_width)
petal_maxlength = max(petal_length)
petal_maxwidth = max(petal_width)
print("花萼长度最大值："+sepal_maxlength+" 花萼宽度最大值："+sepal_maxwidth +
      " 花瓣长度最大值："+petal_maxlength+" 花瓣宽度最大值："+petal_maxwidth)
""" 最小值 """
sepal_minlength = min(sepal_length)
sepal_minwidth = min(sepal_width)
petal_minlength = min(petal_length)
petal_minwidth = min(petal_width)
print("花萼长度最小值："+sepal_minlength+" 花萼宽度最小值："+sepal_minwidth +
      " 花瓣长度最小值："+petal_minlength+" 花瓣宽度最小值："+petal_minwidth)
""" 中位数 """
sepal_midlength = median(sepal_length)
sepal_midwidth = median(sepal_width)
petal_midlength = median(petal_length)
petal_midwidth = median(petal_width)
print("花萼长度中位数："+sepal_midlength+" 花萼宽度中位数："+sepal_midwidth +
      " 花瓣长度中位数："+petal_midlength+" 花瓣宽度中位数："+petal_midwidth)

result = {}
for s in species:
    if s in result.keys():
        result[s] += 1
    else:
        result[s] = 1
plt.pie(result.values(), labels=result.keys(), autopct='%.2f%%')

species1 = np.where(species == "setosa", 0, species)
species2 = np.where(species1 == "versicolor", 1, species1)
species3 = np.where(species2 == "virginica", 2, species2)
print(species3)
