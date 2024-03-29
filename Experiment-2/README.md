# 实验 2 Python 函数的定义与调用

### 实验目的

1. 熟悉并掌握函数的定义和调用
1. 理解函数形参和实参的含义，能够正确设置形参类型
1. 理解隐含函数 lambda

### 实验时间和地点

2 课时，计算机机房 C2-416

实验内容

1. 请使用函数式编程+内置函数来实现： “水仙花数”。

所谓水仙花数是指 1 个 3 位的十进制数，其各位数字的立方和等于该数本身。例如：153 是水仙花数，因为 153 = 13 + 53 + 33 。

1. 编写函数实现：（1）产生一个包含 n 个元素的列表，列表中的每个元素随机产生：参数为列表元素的个数、随机数的最小(默认为 1)和最大取值（默认为 100）。

（2）判断一个数是否为素数  
（3）编写主程序，调用这两个函数，显示产生的列表、列表中所有的素数、素数之和。

1. 计算两点间曼哈顿距离和欧氏距离。
1. 判断密码强度，数字、小写字母、大写字母和指定的标点符号，分别对应 weak、below middle、above middle、strong。
1. 有一个数列，形式为 1 1 1 3 5 9 17 31……。

编写函数计算该数列第 20 项的值。（可以使用递归，并输出执行时间）

1. 编写一个函数实现根据本金、年利率、存款年限计算得到本金和利息的功能。分别使用位置参数和关键字参数来调用这个函数：本金 10000，年利率：5.5%，存 5 年; 本金 10000，年利率：3.5%，存 3 年
1. 将第 6 题改为 lambda 函数，返回本金+收益

### 实验步骤

1. 打开 Spyder 或 Jupyter NoteBook
2. 新建
3. 输入
4. 保存
5. 运行

### 实验注意事项

1. 函数的正确缩进。
1. Lambda 函数的定义和实现。
1. 函数内变量的作用域。
1. 递归调用次数多的时候效率低，如果一定要采用递归形式，使用缓存机制来实现。

如：第 5 题要计算第 500 项的值，执行速度会很慢  
在函数定义前加上：

```python
from functools import lru_cache
@lru_cache(maxsize=10000)
```

### 实验报告要求

    实验报告以电子文档形式提交。

实验报告主要内容：思路（可以是流程图），主要数据结构说明，运行结果和过程记录、**实验总结（不少于 200 字）。**  
**同时提交源代码（独立文件）**
