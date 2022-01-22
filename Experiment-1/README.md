# 实验 1 Python 数据分析环境设置

### 实验目的

1. 掌握 Anaconda 的安装和配置
1. 熟悉 JupyterNotebook、Spyder 工具的使用
1. 编写和执行 Python 源文件程序
1. 在线帮助和相关资源

### 实验时间和地点

2 课时，计算机机房

实验内容

1. 安装 Anaconda；
1. 扩展库的安装；

2、熟悉 Jupyter Notebook 编程环境。
3、熟悉 Spyder 环境
4、编写第一个 Python 程序

### 实验步骤

1. 下载 Anaconda

1. 从官网[https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual) 或[https://anaconda.org/](https://anaconda.org/)或下载最新版 Anaconda3，需要根据安装的 OS 来进行选择。
1. 具体的安装环境要求可以查看官网的文档说明。
1. 如果需要，从www.python.org官网上下载Python。
1. 安装 anaconda
1. 安装时选择定制安装，建议不要把 Anaconda 安装在 C 盘上，安装路径最好不要有中文。
1. 安装时选择针对所有用户。
1. 可以把 Anaconda 自带的 Python 解释器加入到 path 中。
1. 如果想要单独使用 Python 解释器，可以专门下载 Python，安装后设置 Path。
1. 安装第三方库
1. 在 Dos 界面输入 conda list 查看已经安装的库和包
1. 如果没有 scrapy 包，输入 conda install scrapy 进行安装
1. 启动 Spyder

1) 【开始 】-->【所有程序】-->【anaconda】-->【Spyder(anaconda3】。

1. 观察 Spyder 界面，打开【tools】🡪【Preferences】。
1. 可以在【current working directory】设置默认的启动目录等。其他设置使用习惯自己摸索。截图记录
1. 将下列代码录入、保存并执行。观察文件夹、文件创建情况，打开文件。
1. 使用“Variarible explorer” 观察变量,双击 answer，观察变量的变化过程并截图保存。

![](https://cdn.nlark.com/yuque/0/2022/png/23075474/1642830964795-80dde0ce-e09c-4816-8830-bea91729342a.png#)

1. 完成下面代码并观察输出和 plot

![](https://cdn.nlark.com/yuque/0/2022/png/23075474/1642830965216-d8844e43-1285-47f6-b6b1-aa55ea99a36a.png#)

1.  启动 Jupyter Notebook
    1. 【开始 】-->【所有程序】-->【anaconda】-->【Jupyter Notebook】，如果打不开，选择复制链接。
1.  单击【new】--->“Python 3”，进入 Python 脚本编辑界面。

1.  编写第一个 Python 程序

        输入：姓名

    输出：“我是 XX，这是我的第一个 Python 程序。”

### 实验注意事项

1）Python 是解释型语言，需要 Python 解释器支持。  
2）可以使用.tab 来获取对象的属性，使用函数名?获取函数帮助信息，??函数名获取函数源码。

### 实验报告要求

    实验报告以电子文档形式提交。

实验报告主要内容：anaconda 安装过程、第三方扩展库的安装、Python 程序基本结构，运行结果和过程记录、**实验总结。**
