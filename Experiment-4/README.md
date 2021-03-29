# 实验4 NumPy数值计算
## 实验目的
1. 熟悉并掌握NumPy矩阵
2. 使用数组进行简单的统计分析
## 实验时间和地点
2课时，计算机机房C2-416

## 实验内容
1. 使用arange创建一个一维数组，从0到50，步长为3。提取出其中所有的奇数并输出。
2. 将题1数组中所有奇数用-1替换。
3. 输入一个数组，将其转换为2行的数组。
4. 使用ndarray、数组转置和矩阵乘法求1，2，…,n的平方，平方和。
5. Seaborn库自带数据集Iris(鸢尾花卉数据集)，是一类多重变量分析的数据集。数据集包含150个数据集，分为3类，每类50个数据，每个数据包含4个属性。可通过花萼长度，花萼宽度，花瓣长度，花瓣宽度4个属性预测鸢尾花卉属于（Setosa，Versicolour，Virginica）三个种类中的哪一类”。
    - sepal_length:花萼长度，单位cm
    - sepal_width:花萼宽度，单位cm
    - petal_length:花瓣长度，单位cm
    - petal_width:花瓣宽度，单位cm
    - 种类:setosa(山鸢尾)，versicolor(杂色鸢尾)，virginica(弗吉尼亚鸢尾)

    1. 读取Iris数据集中的4个属性，并对花萼长度、花萼宽度、花瓣长度、花瓣宽度进行统计分析，计算它们的均值、标准差、最大值、最小值、中位数
    2. 计算setosa(山鸢尾)，versicolor(杂色鸢尾)，virginica(弗吉尼亚鸢尾)各自的数量，所占比
    3. 将setosa(山鸢尾)，versicolor(杂色鸢尾)，virginica(弗吉尼亚鸢尾)的值分别改为0,1,2
    4. 将前四列随机插入np.nan值20个
    5. 查找缺失值np.nan的数量和位置，并用0替换
## 实验步骤
1. 打开Spyder或Jupyter NoteBook
2. 新建
3. 输入  
方法一：  
```python
import seaborn as sns
iris=sns.load_dataset("iris") #从github上加载iris数据集
iris.head()         #查看数据集的前5行数据
```
方法二：  
如果长时间没有加载成功，可以下载文件https://github.com/mwaskom/seaborn-data/blob/master/iris.csv，  
```python
Datas3=np.loadtxt('iris.csv',delimiter=",",skiprows=1,usecols=[0,1,2,3])
datas4=np.loadtxt('iris.csv',delimiter=",",skiprows=1,dtype=str,encoding='UTF-8',usecols=[4])
```
方法三：  
或使用下列方法访问  
```python
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris= np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3]) #获取数据集的前4列
```
后面加上自己的代码。  
4. 保存
5. 运行
