# 实验8 Scikit-learn构建聚类模型

### 实验目的

1.  使用sklearn估计器构建K-Means聚类模型

2.  根据聚类模型评价指标对K-Means聚类模型进行评价

3.  编写Python关联分析代码，并应用。

### 实验时间和地点

> 2课时，计算机机房C2-416

**实验内容**

1.  使用关联规则分析购物车

> 数据整理自一家中等化妆品在线商店公布的网上公开数据集，为该化妆品商店真实的用户交易信息，数据集中每一行表示一个事件，所有的事件都与商品和用户相关，并且用户的点击行为之间是有时间顺序的。数据集中包含了商品和用户的多个属性，例如商品编号、商品类别、用户编号、事件时间等。

文件字段说明:

  **名称**        **标签**
--------------- ---------------------------------------------------------------
  event_time      When event is was happened
  event_type      Event type: one of \[view, cart, remove_from_cart, purchase\]
  product_id      Product ID
  category_id     Product category ID
  category_code   Category meaningful name (if present)
  brand           Brand name in lower case (if present)
  price           Product price
  user_id         Permanent user ID
  user_session    User session ID

要求完成：对train.csv的购物车商品（可以忽略行为）进行**关联规则分析**，找到最受欢迎的商品组合（多种）。试试为test.csv中的客户推荐商品。实际数据和赛题要求来源于以下网址：[电商用户购买行为预测 竞赛 - DataFountain](https://www.datafountain.cn/competitions/482)

2.  构建基于scikit-learn的k- Means聚类模型

> 数据来源：[UCI Machine Learning Repository: Wine Data Set](http://archive.ics.uci.edu/ml/datasets/Wine)

wine数据集是和酒有关的数据集。wine数据集包含3种 同起源的葡萄酒的记录,共178条，

class 1 59

class 2 71

class 3 48。

其中,每个特征对应葡萄酒的每种化学成分,并且都 属于连续型数据。通过化学分析可以推断葡萄酒的起源。

要求：wine数据集的葡萄酒总共分为3种,通过将wine数据集的数据进行聚类,聚集为3 个簇,能够实现葡萄酒的类别划分，可视化显示并对聚类模型进行评价

### 实验原理（理论支持）

-   题目1只要求对购物车中的商品进行关联规则，简单处理方式就是只取用户号和商品编号。

-   题目2的思路是先进行数据预处理------\>构建聚类数目为3的- -Means模型------\>评估模型------\>可视化

### 实验步骤 

1\. 打开Spyder或Jupyter NoteBook

2\. 新建

3.输入

4.保存

5.运行

### 实验报告要求

实验报告以电子文档形式提交。

实验报告主要内容：**思路（重点，说明处理的方式、原因和效果）**，主要数据结构说明，运行结果和过程记录、**实验总结（不少于200字）。**

**同时提交源代码（独立文件）**
