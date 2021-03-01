# 实验1   Python数据分析环境设置
## 实验目的
1. 掌握Anaconda的安装和配置
2. 熟悉JupyterNotebook、Spyder工具的使用
3. 编写和执行Python源文件程序
4. 在线帮助和相关资源

## 实验时间和地点
2课时，计算机机房

## 实验内容
1. 安装Anaconda；
2. 扩展库的安装；
3. 熟悉Jupyter Notebook编程环境。
4. 熟悉Spyder环境
5. 编写第一个Python程序

## 实验步骤
1. 下载Anaconda
    1. 从官网https://www.anaconda.com/products/individual 或https://anaconda.org/ 或下载最新版Anaconda3，需要根据安装的OS来进行选择。
    2. 具体的安装环境要求可以查看官网的文档说明。
    3. 如果需要，从 www.python.org 官网上下载Python。
    
2. 安装anaconda
    1. 安装时选择定制安装，建议不要把Anaconda安装在C盘上，安装路径最好不要有中文。
    2. 安装时选择针对所有用户。
    3. 可以把Anaconda自带的Python解释器加入到path中。
    4. 如果想要单独使用Python解释器，可以专门下载Python，安装后设置Path。
    
3. 安装第三方库
    1. 在Dos界面输入conda list查看已经安装的库和包
    2. 如果没有scrapy包，输入conda install scrapy进行安装
    
4. 启动Spyder
    1. 【开始 】-->【所有程序】-->【anaconda】-->【Spyder(anaconda3】。
    2. 观察Spyder界面，打开【tools】-->【Preferences】。
    3. 可以在【current working directory】设置默认的启动目录等。其他设置使用习惯自己摸索。截图记录
    4. 将下列代码录入、保存并执行。观察文件夹、文件创建情况，打开文件。
    5. 使用“Variarible explorer” 观察变量,双击answer，观察变量的变化过程并截图保存。
    ```python
    #Febonacci swquence
    '''
    斐波那契数列
    输入：项数n
    输出：前n项
    '''
    import os
    def fibo(n):
        numbers=[1,1]
        for i in range(n-2):
            numbers.append(number[i]+numbers[i+1])
        return numbers
    answer=fibo(10)
    print(answer)
    if not os.path.exists('result'):
        os.mkdir('result')
    file=open('result/fibo.txt','w')
    for num in answer:
        file.write(str(num)+' ')
    file.close()
    ```
    
5. 完成下面代码并观察输出和plot
```python
import matplotlib.pyplot as plt
import random
gradewords=('优秀','良好','中等','及格','不及格')
testwords=[random.choice(gradewords) for i in range(1000)]
result=dict()
for item in testwords:
    if item in testwords:
        result[item]=result.get(item,0)+1
for key,v,int result.items():
    print(key,v,sep='--->')
plt.pie(result.values(),labels=result.keys(),autopct='%.2f%%')
plt.show()
```
6. 启动Jupyter Notebook
    1. 【开始】-->【所有程序】-->【anaconda】-->【Jupyter Notebook】，如果打不开，选择复制链接。
    2. 单击【new】--->“Python 3”，进入Python脚本编辑界面。

7. 编写第一个Python程序  
    输入：姓名  
    输出：“我是XX，这是我的第一个Python程序。”

## 实验注意事项
1. Python是解释型语言，需要Python解释器支持。
2. 可以使用.tab来获取对象的属性，使用函数名?获取函数帮助信息，??函数名获取函数源码。

## 实验报告要求
实验报告以电子文档形式提交。
实验报告主要内容：anaconda安装过程、第三方扩展库的安装、Python程序基本结构，运行结果和过程记录、实验总结。