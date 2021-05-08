**实验6 Pandas数据读写与聚合**

### 实验目的

1.  读写不同数据源的数据

2.  聚合数据。

### 实验时间和地点

> 2课时，计算机机房C2-416

**实验内容**

（一）数据来源是美国华盛顿2011到2012年使用共享单车的数据，本次实验用到train.csv和test.csv。数据来源：https://www.kaggle.com/c/bike-sharing-demand

变量说明

> datetime（日期） - hourly date + timestamp
>
> season（季节） - 1 = spring, 2 = summer, 3 = fall, 4 = winter
>
> holiday（是否假日） - whether the day is considered a holiday
>
> workingday（是否工作日） - whether the day is neither a weekend nor holiday
>
> weather（天气等级） - （1）: Clear, Few clouds, Partly cloudy 清澈，少云，多云。
>
> （2）: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist 雾+阴天，雾+碎云、雾+少云、雾
>
> （3）: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds 小雪、小雨+雷暴+散云，小雨+云
>
> （4）: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog 暴雨+冰雹+雷暴+雾，雪+雾
>
> temp（温度） - temperature in Celsius
>
> atemp（体感温度） - \"feels like\" temperature in Celsius
>
> humidity（相对湿度） - relative humidity
>
> windspeed（风速） - wind speed
>
> casual（临时租赁数量） - number of non-registered user rentals initiated
>
> registered（会员租赁数量） - number of registered user rentals initiated
>
> count（总租赁数量） - number of total rentals
>
> 完成以下操作：

1.  导入数据

2.  查看数据信息

3.  在train.csv中，将时段转换成日期时间型，分为：年份，月份，星期，并完成以下数据探索和处理

```{=html}
<!-- -->
```
1.  计算出每天的租车人数，以拆线图显示每天的租车人数

2.  计算会员租车人次和非会员租车人次，并以饼图显示出来

3.  根据工作日、休息日以折线图显示不同时间段的租车人数

4.  去除count 3个标准差以外的数据（行）

5.  画出气温和租赁人数的关系

```{=html}
<!-- -->
```
4.  合并两个数据集，注意列的对齐，查看合并后的数据集，将时段转换成日期时间型，分为：年份，月份，星期，并完成

```{=html}
<!-- -->
```
1.  删除列atem, humidity, casual, registered

2.  以前/后一天数据填充空值，或以本月中现在是周几的平均值进行填充（麻烦，难）

3.  将风速为0的值替换为平均值

```{=html}
<!-- -->
```
5.  将4得到的数据保存在在硬盘上

（二）使用iris数据集，读取并完成：

1、查看数据集的维度、大小等信息

2、使用describe方法对整个mpg数据集描述性统计

3、以species分类显示sepal_length，sepal_width，petal_length, petal_width的均值、标准差

4、添加两列，值分别为：sepal_length/ sepal_width，petal_length/petal_width，并分类显示出来

### 实验原理（理论支持）

1.  引用seaborn 库

import seaborn as sns

data_iris=sns.load_dataset(\"iris\")

常见的缺失值处理方法

  方法名      含义
----------- -----------------------------------------------
  isnull()    判断每个元素是否为空/缺失值，返回一个布尔数组
  notnull()   判断每个元素是否为非空，返回一个布尔数组
  fillna()    设置缺失值的填补方法，返回一个新的对象
  dropna()    删除缺失值

聚合运算方法

  方法     含义                         方法          含义
-------- ---------------------------- ------------- --------------------------------
  count    计算分组的数目，包括缺失值   std、var      返回每组的标准差、方差
  sum      返回每组的和                 min、max      返回每组的最小值、最大值
  mean     返回每组的平均值             prod          返回每组的乘积
  median   返回每组的算术中位数         first、last   返回每组的第一个值、最后一个值
  idxmax   返回每组最大值所在索引       idxmin        返回每组最小值所在的索引
  median   返回每组中位数               describe      返回描述性统计信息

### 实验步骤 

1\. 打开Spyder或Jupyter NoteBook

2\. 新建

3.输入

4.保存

5.运行

### 实验注意事项

1.  如果使用Jupyter NoteBook，在代码第一行加入指令 %matplotlib inline，以确保图形能够在浏览器中显示。

2.  如果要将图形存盘，使用如下代码：plt.savefig(r\"d:\\test2.jpg\",dpi=1000,bbox_inches=\'tight\',pad_inches=0) 。

### 实验报告要求

实验报告以电子文档形式提交。

实验报告主要内容：思路，主要数据结构说明，运行结果和过程记录、**实验总结（不少于200字）。**

**同时提交源代码（独立文件）**