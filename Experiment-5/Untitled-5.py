import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('1980_2016_retrieved_TCsize_2Pub_v2.csv',
                  delimiter=',', skiprows=1, usecols=[0, 1, 2, 3, 4, 5])
dataT = data.T
YYYYNNMMDDHH = dataT[0]  # YYYY年份，NN序号，MM月份，DD日期，HH小时
LAT = dataT[1]  # 纬度
LONG = dataT[2]  # 经度
SiR34 = dataT[5]  # 尺度
x = LONG
y = LAT
z = SiR34
plt.scatter(x, y, s=(z-min(z)+0.1), c=z)
plt.show()
