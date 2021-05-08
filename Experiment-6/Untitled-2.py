# In[0]:
from pandas.io.parsers import read_csv
iris = read_csv("./seaborn-data-master/iris.csv", sep=",")
# In[1]:
print(iris.shape)
print(iris.size)
# In[2]:
mpg = read_csv("./seaborn-data-master/mpg.csv", sep=",")
print(mpg.describe())
# In[3]:
print("均值：")
print(iris.groupby(['species']).mean())
print("标准差：")
print(iris.groupby(['species']).std())
# In[4]:
iris['sepal_length/sepal_width'] = iris['sepal_length']/iris['sepal_width']
iris['petal_length/petal_width'] = iris['petal_length']/iris['petal_width']
print(iris)
