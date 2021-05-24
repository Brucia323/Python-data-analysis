import matplotlib.pyplot as plt
import numpy as np
from numpy import isnan, nan, random, where
from numpy.core.fromnumeric import size, std
from numpy.lib.function_base import median

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
print("花萼长度均值："+str(sepal_avglength)+" 花萼宽度均值："+str(sepal_avgwidth) +
      " 花瓣长度均值："+str(petal_avglength)+" 花瓣宽度均值："+str(petal_avgwidth))
""" 标准差 """
sepal_stdlength = std(sepal_length)
sepal_stdwidth = std(sepal_width)
petal_stdlength = std(petal_length)
petal_stdwidth = std(petal_width)
print("花萼长度标准差："+str(sepal_stdlength)+" 花萼宽度标准差："+str(sepal_stdwidth) +
      " 花瓣长度标准差："+str(petal_stdlength)+" 花瓣宽度标准差："+str(petal_stdwidth))
""" 最大值 """
sepal_maxlength = max(sepal_length)
sepal_maxwidth = max(sepal_width)
petal_maxlength = max(petal_length)
petal_maxwidth = max(petal_width)
print("花萼长度最大值："+str(sepal_maxlength)+" 花萼宽度最大值："+str(sepal_maxwidth) +
      " 花瓣长度最大值："+str(petal_maxlength)+" 花瓣宽度最大值："+str(petal_maxwidth))
""" 最小值 """
sepal_minlength = min(sepal_length)
sepal_minwidth = min(sepal_width)
petal_minlength = min(petal_length)
petal_minwidth = min(petal_width)
print("花萼长度最小值："+str(sepal_minlength)+" 花萼宽度最小值："+str(sepal_minwidth) +
      " 花瓣长度最小值："+str(petal_minlength)+" 花瓣宽度最小值："+str(petal_minwidth))
""" 中位数 """
sepal_midlength = median(sepal_length)
sepal_midwidth = median(sepal_width)
petal_midlength = median(petal_length)
petal_midwidth = median(petal_width)
print("花萼长度中位数："+str(sepal_midlength)+" 花萼宽度中位数："+str(sepal_midwidth) +
      " 花瓣长度中位数："+str(petal_midlength)+" 花瓣宽度中位数："+str(petal_midwidth))

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

sepal_length[np.random.choice(size(sepal_length), 20)] = np.nan
sepal_width[random.choice(size(sepal_width), 20)] = np.nan
petal_length[random.choice(size(petal_length), 20)] = nan
petal_width[random.choice(size(petal_width), 20)] = nan
print("花萼长度缺失值数量：\n", isnan(sepal_length).sum())
print("花萼长度缺失值位置：\n", where(isnan(sepal_length)))
sepal_length[isnan(sepal_length)] = 0
print("花萼宽度缺失值数量：\n", isnan(sepal_width).sum())
print("花萼宽度缺失值位置：\n", where(isnan(sepal_width)))
sepal_width[isnan(sepal_width)] = 0
print("花瓣长度缺失值数量：\n", isnan(petal_length).sum())
print("花瓣长度缺失值位置：\n", where(isnan(petal_length)))
petal_length[isnan(petal_length)] = 0
print("花瓣宽度缺失值数量：\n", isnan(petal_width).sum())
print("花瓣宽度缺失值位置：\n", where(isnan(petal_width)))
petal_width[isnan(petal_width)] = 0

print(sepal_length)
print(sepal_width)
print(petal_length)
print(petal_width)
