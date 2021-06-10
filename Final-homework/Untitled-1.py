from numpy import where
from pandas.core.frame import DataFrame
from sklearn.cluster import KMeans
from pylab import mpl
from matplotlib.pyplot import bar, figure, legend, pie, plot, scatter, show, subplot, title
from datetime import datetime
from pandas import read_csv, to_datetime

data1 = read_csv("data1.csv", encoding='GB18030')
data2 = read_csv("data2.csv", encoding='GB18030')
data3 = read_csv("data3.csv", encoding='GB18030')
print(data1.head(3))
print(data2.head(3))
print(data3.head(3))
data1 = data1.drop('Index', axis=1)
data2 = data2.drop('Index', axis=1)
data3 = data3.drop('Index', axis=1)
data2 = data2.drop('PeoNo', axis=1)
data2 = data2.drop('TermNo', axis=1)
data2 = data2.drop('TermSerNo', axis=1)
data2 = data2.drop('conOperNo', axis=1)
data2 = data2.drop('OperNo', axis=1)
data3 = data3.drop('Describe', axis=1)
data1.columns = ['卡号', '性别', '专业', '门禁卡号']
data2.columns = ['卡号', '时间', '消费金额', '存款金额', '结余', '刷卡次数', '类型', '部门']
data3.columns = ['门禁卡号', '时间', '地点', '访问']
print(data1.isnull().any())
print(data2.isnull().any())
print(data3.isnull().any())
data4 = data2[data2['类型'] == '消费']
date1 = to_datetime(data4['时间'])
time1 = date1.apply(lambda x: datetime.strftime(x, "%H"))
data4['时间（时）'] = time1
mpl.rcParams['font.sans-serif'] = ['simhei']
plot(data4.groupby('时间（时）').count())
title("消费人数")
show()
plot(data4.groupby('时间（时）')['消费金额'].sum())
title("消费金额")
show()
data5 = data4[data4['部门'] == '第一食堂']
data5 = data5.append(data4[data4['部门'] == '第二食堂'])
data5 = data5.append(data4[data4['部门'] == '第三食堂'])
data5 = data5.append(data4[data4['部门'] == '第四食堂'])
data5 = data5.append(data4[data4['部门'] == '第五食堂'])
pie(data5.groupby('部门')['部门'].count(), labels=[
    '第一食堂', '第三食堂', '第二食堂', '第五食堂', '第四食堂'])
show()
pie(data5.groupby('部门')['消费金额'].sum(), labels=[
    '第一食堂', '第三食堂', '第二食堂', '第五食堂', '第四食堂'])
show()
data6 = DataFrame()
data6 = data4.groupby('卡号')['消费金额', '结余'].sum()
data7 = DataFrame()
data7['卡号'] = data4['卡号'].drop_duplicates()
n_clusters = 3
k = KMeans(n_clusters=n_clusters)
k.fit(data6)
y_pred = k.predict(data6)
bar(y_pred, data6['消费金额'], label='消费金额')
legend()
show()
