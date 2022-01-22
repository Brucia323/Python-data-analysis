# 实验 5 Matplotlib 数据可视化

### 实验目的

1. 熟悉并掌握 matplotlib 库的使用
1. 理解函 pyplot 绘图方法

掌握折线图、饼图、散点图、柱形图、气泡图、条形图、直方图的作用与绘制方法。

1. 根据数据特点，采用不同类型的图型进行可视化处理。

### 实验时间和地点

2 课时，计算机机房 C2-416

实验内容

1. 绘制一个包含 4 个子图的图形，分别显示 sin, cos, log 和 exp，可以设置以下取值和参数，自己可上标题、x、y 轴标签等内容，线型和颜色自定

```python
x=np.linspace(0,2\*math.pi);
plt.rcParams['font.sans-serif']=['KaiTi'] #SIMHei 黑体
plt.rcParams['axes.unicode_minus']=False #正常显示图中负号
```

1. 数据:某明星在某平台的红黑粉数据

日期 红粉数 黑粉数  
2020.03.30 152577 17165  
2020.03.31 142709 9361  
2020.04.01 128653 9964  
2020.04.02 134998 6537  
2020.04.03 139483 6043  
2020.04.04 99846 5723  
2020.04.05 141211 13157  
2020.04.06 151192 8632  
2020.04.07 160863 5723  
（1）请根据数据画出拆线图，其中红粉用红色，黑粉用黑色。要求有网络线  
（2）根据数据绘制柱形图  
（3）4 月 7 日年龄和性别分布情况(%)  
红粉 黑粉  
18 岁以下 0.91 1.76  
18-24 岁 16.79 29.58  
25-34 岁 66.14 60.92  
35-44 岁 13.68 5.28  
45-54 岁 2.12 1.41  
55 岁及以上 0.36 1.05  
男 10.32 24.42  
女 89.68 73.58  
请根据数据绘制条形图和饼图

1. 1980_2016_retrieved_TCsize_2Pub_v2.csv 是**卫星分析热带气旋尺度资料，请根据经度纬度画出气旋的散点图（如 2020 年）**

**根据经度、纬度、**热带气旋的尺度或最大风速（或其他属性）画出气泡图（某一个热带气旋），尺度或最大风速越大，点的面积越大。  
**包含的数据内容如下：**  
**资料文件内容格式**![](https://cdn.nlark.com/yuque/0/2022/jpeg/23075474/1642831022804-7dc7a770-a97d-4399-8976-f3e51a59d6f1.jpeg#)

| YYYY   | 年份;                                                                                       |
| ------ | ------------------------------------------------------------------------------------------- |
| NN     | 包括热带低压在内的热带气旋序号;                                                             |
| MMDDHH | 2 位数月份、2 位数日期、2 位数小时（世界时）;                                               |
| LAT    | 热带气旋中心纬度，IBTrACS v03r02: Basin.WP.ibtracs_all.v03r08.csv;                          |
| LONG   | 热带气旋中心经度，IBTrACS v03r02: Basin.WP.ibtracs_all.v03r08.csv;                          |
| PRS    | 热带气旋中心最低气压，IBTrACS v03r02: Basin.WP.ibtracs_all.v03r08.csv;                      |
| WND    | 热带气旋近中心最大风速，取自 IBTrACS v03r02: Basin.WP.ibtracs_all.v03r08.csv;               |
| SiR34  | 热带气旋的尺度(km, 以 34 海里/小时风圈半径为准).                                            |
| SATSer | 用于反演的卫星，包括 GOES-1 ～ 13, Meteosat-2 ～ 9, GMS-1 ～ 5、MTSAT-1R, MTS-2,和 FY2-C/E. |

### 实验原理（理论支持）

1. 导入 matplotlib.pyplot
1. 使用 matplotlib 库提供的函数来编写代码。
1. 绘制子图

   - 在 matplotlib 中绘图是在当前图形（figure）和当前坐标系（axes）中进行，默认在一个编号为 1 的 figure 中绘图，可以在一个图的多个区域分别绘图
   - 可以使用 subplot()/subplots 函数和 axes()函数

1. 使用 subplot()

![](https://cdn.nlark.com/yuque/0/2022/png/23075474/1642831023338-2ab80c5f-437d-4efc-bcb9-2a17a8f776b8.png#)  
图 1 2 行 1 列

```python
plt.subplot(211) #2 行 1 列第 1 小图
plt.plot(x,C) #绘制余弦曲线
plt.subplot(212) #2 行 1 列第 2 小图
plt.plot(x,S) #绘制正弦弦曲线
```

![](https://cdn.nlark.com/yuque/0/2022/png/23075474/1642831023824-40a8a21a-c22e-46c4-bf1d-f3fc10744f83.png#)  
图 2 1 行 2 列

```python
plt.subplot(121) #1 行 2 列第 1 小图
plt.plot(x,C) #绘制余弦曲线
plt.subplot(122) #1 行 2 列第 2 小图
plt.plot(x,S) #绘制正弦弦曲线
```

图 3 2 行 2 列

```python
plt.subplot(221) #2 行 2 列第 1 小图
plt.plot(x,C)
plt.subplot(222) #2 行 2 列第 2 小图
plt.plot(x,S)
plt.subplot(223) #2 行 2 列第 3 小图
plt.plot(x,x*x)
plt.subplot(224) #2 行 2 列第 4 小图
plt.plot(x,x+9)
```

![](https://cdn.nlark.com/yuque/0/2022/png/23075474/1642831024311-0f669d01-d1d6-4bae-bccf-7b1ecc97d6bc.png#)

![](https://cdn.nlark.com/yuque/0/2022/png/23075474/1642831024548-50018cf2-8f12-4b13-be76-70930b38f037.png#)  
图 4 2 行 3 列

```python
plt.subplot(2,1,1) #2 行 1 列第 1 小图（整个图像窗口分为 2 行 1 列, 第 1 个小图占用了第 1 个位置, 也就是整个第 1 行。）
plt.plot([0,1],[0,1])
plt.subplot(234) #2 行 3 列第 4 小图（将整个图像窗口分为 2 行 3 列, 于是整个图像窗口的第 1 行就变成了 3 列, 也就是成了 3 个位置, 于是第 2 行的第 1 个位置是整个图像窗口的第 4 个位置。）
plt.plot([0,1],[0,2])
plt.subplot(2,3,5) #2 行 3 列第 5 小图
plt.plot([0,1],[0,3])
plt.subplot(2,3,6) #2 行 3 列第 6 小图
plt.plot([0,1],[0,4])
```

1. subplots()可以指定子图是几行几列

fig,(ax0,ax1)=plt.subplots(2,1)  
fig：图对象本身  
(ax0,ax1)两个子图，有名称，可以分别为子图设置标题等，一般要设置子图间的距离  
![](https://cdn.nlark.com/yuque/0/2022/png/23075474/1642831024848-0fe077c6-45c6-4a38-aa13-12e7a886b4d8.png#)

```python
x=np.linspace(-np.pi,np.pi,300)
fig,(ax0,ax1)=plt.subplots(2,1)#子图包含 2 行 1 列
ax0.plot(x,np.sin(x),'r')
ax0.set_title('正弦函数')
plt.subplots_adjust(hspace=0.5)#垂直方向距离
ax1.plot(x,np.cos(x),'g')
ax1.set_title('余弦函数')
```

1. axes()

axes([left,bottom,width,height])参数范围为(0,1),表示相对坐标轴的百分比距离

![](https://cdn.nlark.com/yuque/0/2022/png/23075474/1642831025091-bceca5f1-5527-460e-8d80-9590e7b19778.png#)

```python
plt.axes([.1,.1,.8,.8])
plt.plot(x,np.sin(x),'r')
plt.axes([.3,.15,.4,.3])
plt.plot(x,np.cos(x),'g')
```

### 实验步骤

1. 打开 Spyder 或 Jupyter NoteBook
2. 新建 3.输入 4.保存 5.运行

### 实验注意事项

1. 如果使用 Jupyter NoteBook，在代码第一行加入指令  %matplotlib inline，以确保图形能够在浏览器中显示。
1. 如果要将图形存盘，使用如下代码：plt.savefig(r"d:\test2.jpg",dpi=1000,bbox_inches='tight',pad_inches=0) 。

### 实验报告要求

    实验报告以电子文档形式提交。

实验报告主要内容：思路（可以是流程图），主要数据结构说明，运行结果和过程记录、**实验总结（不少于 200 字）。说明在什么情况下适合什么样的图表**  
**同时提交源代码（独立文件）**
