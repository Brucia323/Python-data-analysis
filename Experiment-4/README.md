# 实验 4 NumPy 数值计算

### 实验目的

1.    熟悉并掌握 NumPy 矩阵  
2.    使用数组进行简单的统计分析

### 实验时间和地点

2 课时，计算机机房 C2-416

实验内容  
1．  使用 arange 创建一个一维数组，从 0 到 50，步长为 3。提取出其中所有的奇数并输出。  
2．  将题 1 数组中所有奇数用-1 替换。  
3．  输入一个数组，将其转换为 2 行的数组。  
4．  使用 ndarray、数组转置和矩阵乘法求 1，2，…,n 的平方，平方和。  
5． Seaborn 库自带数据集 Iris(鸢尾花卉数据集)，是一类多重变量分析的数据集。数据集包含 150 个数据集，分为 3 类，每类 50 个数据，每个数据包含 4 个属性。可通过花萼长度，花萼宽度，花瓣长度，花瓣宽度 4 个属性预测鸢尾花卉属于（Setosa，Versicolour，Virginica）三个种类中的哪一类”。  
·                 sepal_length:花萼长度，单位 cm  
·                 sepal_width:花萼宽度，单位 cm  
·                 petal_length:花瓣长度，单位 cm  
·                 petal_width:花瓣宽度，单位 cm  
·                  种类:setosa(山鸢尾)，versicolor(杂色鸢尾)，virginica(弗吉尼亚鸢尾)

（1）     读取 Iris 数据集中的 4 个属性，并对花萼长度、花萼宽度、花瓣长度、花瓣宽度进行统计分析，计算它们的均值、标准差、最大值、最小值、中位数  
（2）     计算 setosa(山鸢尾)，versicolor(杂色鸢尾)，virginica(弗吉尼亚鸢尾)各自的数量，所占比  
（3）     将 setosa(山鸢尾)，versicolor(杂色鸢尾)，virginica(弗吉尼亚鸢尾)的值分别改为 0,1,2  
（4）     将前四列随机插入 np.nan 值 20 个  
（5）     查找缺失值 np.nan 的数量和位置，并用 0 替换

### 实验步骤

1.  打开 Spyder 或 Jupyter NoteBook
2.  新建 3.输入

### 方法一

```python
import seaborn as sns
iris=sns.load_dataset("iris") #从 github 上加载 iris 数据集
iris.head()         #查看数据集的前 5 行数据
```

### 方法二

如果长时间没有加载成功，可以下载文件[https://github.com/mwaskom/seaborn-data/blob/master/iris.csv](https://github.com/mwaskom/seaborn-data/blob/master/iris.csv)，

```python
Datas3=np.loadtxt('iris.csv',delimiter=",",skiprows=1,usecols=[0,1,2,3])
datas4=np.loadtxt('iris.csv',delimiter=",",skiprows=1,dtype=str,encoding='UTF-8',usecols=[4])
```

### 方法三

或使用下列方法访问

```python
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris= np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3]) #获取数据集的前 4 列
```

后面加上自己的代码。 4.保存 5.运行
